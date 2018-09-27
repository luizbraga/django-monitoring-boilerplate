from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]

admin.site.site_title = 'project_name'
admin.site.site_header = 'project_name'