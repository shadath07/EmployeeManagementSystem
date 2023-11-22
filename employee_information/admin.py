from django.contrib import admin
from employee_information.models import Department, Position, Employees

# Register your models here.

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id','name','description','status','date_added','date_updated')

class PositionAdmin(admin.ModelAdmin):
    list_display = ('id','name','description','status','date_added','date_updated')
    
class EmployeesAdmin(admin.ModelAdmin):
    list_display = ('id','code','firstname','lastname','gender','dob','contact','address','email','department_id','position_id','date_hired','salary','status','date_added','date_updated')
    
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Position, PositionAdmin)
admin.site.register(Employees, EmployeesAdmin)


admin.site.site_header = 'Employee Management System Admin'
admin.site.site_title = 'Employee Management System Admin'
admin.site.index_title = 'Welcome to Employee Management System Admin'