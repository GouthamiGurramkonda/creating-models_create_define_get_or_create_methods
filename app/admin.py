from django.contrib import admin

# Register your models here.

from app.models import *

admin.site.register(Topic)
def __str__(self):
    return Topic.topic_name


admin.site.register(Webpage)

def __str__(self):
    return Webpage.name

admin.site.register(AccessRecords)

def __str__(self):
    return AccessRecords.author
