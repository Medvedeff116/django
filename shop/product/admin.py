from django.contrib import admin

from .models import *

#admin.site.register(Notebook)

class Memory_typeAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    #list_filter = ('name__name'
admin.site.register(Memory_type,Memory_typeAdmin)

class NotebookAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    #list_filter = ()
admin.site.register(Notebook,NotebookAdmin)