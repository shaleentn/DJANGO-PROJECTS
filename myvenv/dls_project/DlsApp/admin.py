from django.contrib import admin

from . models import Faculty, Department, UserProfile, Resource

# Register your models here.

admin.site.register(Faculty)
admin.site.register(Department)
admin.site.register(UserProfile)
admin.site.register(Resource)