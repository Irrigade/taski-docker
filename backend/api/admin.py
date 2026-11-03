from django.contrib import admin

from .models import Task

admin.site.site_header = "Taski Administration"
admin.site.site_title = "Taski"
admin.site.index_title = "Taski"


class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed')


admin.site.register(Task, TaskAdmin)
