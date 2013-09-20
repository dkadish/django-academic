from django.contrib import admin
from django import forms
from django.db import models
from django.conf import settings

from academic.apps.content.models import *

admin.site.register(Download)
