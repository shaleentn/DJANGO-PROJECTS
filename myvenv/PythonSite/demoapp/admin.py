from django.contrib import admin

# Register your models here.

from . models import Contact, Employee, Department, Student

# admin.site.register(Contact)

@admin.register(Contact)


class ContactAdmin(admin.ModelAdmin):

    list_display=(
        'phone_no', 'address'
    )


# admin.site.register(Employee)
@admin.register(Employee)

class EmployeeAdmin(admin.ModelAdmin):
    list_display=(
        'name', 'contact'
    )

# admin.site.register(Department)
@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display=(
        'name', 'description'
    )

admin.site.register(Student)
