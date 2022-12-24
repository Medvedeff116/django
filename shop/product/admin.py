from django.contrib import admin

from .models import *

#admin.site.register(Notebook)

class Memory_typeAdmin(admin.ModelAdmin):
    list_display = ('id','name')

admin.site.register(Memory_type,Memory_typeAdmin)


class NotebookAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    def get_memory_type(self, obj):
        return obj.Memory_type.name
admin.site.register(Notebook,NotebookAdmin)

class Cpu_typeAdmin(admin.ModelAdmin):
    list_display = ['id','name']

admin.site.register(Cpu_type,Cpu_typeAdmin)

class Video_typeAdmin(admin.ModelAdmin):
    list_display = ['id','name']

admin.site.register(Video_type,Video_typeAdmin)