from django.contrib import admin

# Register your models here.
from app.models import *
class WebpageAdminView(admin.ModelAdmin):
    list_display=['topic_name','name','url']
    list_per_page=['url']
    list_display=['name']
    list_editable=['name']
    list_fields=['name']
    list_filter=['url','name','topic_name']
admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(Access_Records)
