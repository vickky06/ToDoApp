from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Todo
import csv
from django.http import HttpResponse

# Register your models here.
admin.site.site_header = "TODO App:Admin"
class TodoAdmin(admin.ModelAdmin):
    actions = ['export_as_csv']
    list_display = ('title','created','Time','deletion')
    list_filter = ('created','title','deletion')
    search_fields = ('title','created','Time','deletion','description')
    def export_as_csv(self,request,queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_as_csv.short_description = "Export Selected"



admin.site.register(Todo,TodoAdmin)
admin.site.unregister(Group)