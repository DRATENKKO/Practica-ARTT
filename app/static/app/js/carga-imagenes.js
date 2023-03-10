const dropArea = document.querySelector(".drop-area");
const dragText = dropArea.querySelector("h2");
const button = dropArea.querySelector("button");
const input = dropArea.querySelector("#input-file");
let files;


button.addEventListener('click', e => {
    //console.log("click");
    input.click();
});

input.addEventListener('change', (e) => {
    files = input.files;
    dropArea.classList.add("active");
    showFiles(files);
    dropArea.classList.remove("active");
});

dropArea.addEventListener("dragover", (e) => {
    e.preventDefault();
    dropArea.classList.add("active");
    dragText.textContent = "Suelta para cargar los Archivos"
});


dropArea.addEventListener("dragleave", (e) => {
    e.preventDefault();
    dropArea.classList.remove("active");
    dragText.textContent = "Arrastra para cargar los Archivos"
});

dropArea.addEventListener("drop", (e) => {
    e.preventDefault();
    files = e.dataTransfer.files;
    showFiles(files);
    dropArea.classList.remove("active");
    dragText.textContent = "Arrastra para cargar los Archivos"
});



function showFiles(files) {
    if (files.length == undefined) {
        processFile(files);
    } else {
        for (const file of files) {
            processFile(file);
        }
    }
}

function processFile(file) {
    const docType = file.type;
    const validExtensions = ['image/jpeg', 'image/jpg', 'image/png', 'iamge/gif'];

    if (validExtensions.includes(docType)) {
        //archivo valido
        const fileReader = new FileReader();
        const id = `file-${Math.random().toString(32).substring(7)}`;

        fileReader.addEventListener("load", (e) => {
            const fileUrl = fileReader.result;
            const image = `
                <div id="${id}" class="file-container">
                    <img src="${fileUrl}" alt="${file.name}" width="60" height="60">
                </div>
                `;
            console.log(fileUrl);
            const html = document.querySelector("#preview").innerHTML;
            document.querySelector("#preview").innerHTML = image + html;
        });
        fileReader.readAsDataURL(file);
        // uploadFile(file, id);
        document.getElementById('imagen').value = file.name;

    } else {
        //archivo no valido
        alert("no es una archivo valido")
    }
}

async function uploadFile(file) {
    const formData = new FormData();
    formData.append("file", file);

    try {
        const response = await fetch('http://localhost:3000/upload', {
            method: "POST",
            body: formData,
        });
        const responseText = await response.text();
        console.log(responseText);
        document.querySelector(
            `#${id} .status-text`
        ).innerHTML = `<span class="success">Archivo subido correctamente</span>`
    } catch (error) {
        document.querySelector(
            `#${id} .status-text`
        ).innerHTML = `<span class="failure">Error al subir el archivo</span>`
    }
}