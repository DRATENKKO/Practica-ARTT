
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('grilla6x6/', grilla6x6, name="grilla6x6"),
    path('memorama/', memorama, name="memorama"),
    path('sopaletras/', sopaletras, name="sopaletras"),
]