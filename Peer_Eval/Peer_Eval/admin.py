from django.contrib import admin
from django.contrib.admin import AdminSite
from dynamic_forms.admin import FormModel,FormModelAdmin,FormModelData,FormModelDataAdmin

from .models import *

admin.site.register(project)
class ManagerAdmin(AdminSite):
    login_template = 'login.html'

manager_admin = ManagerAdmin(name='manageradmin')
manager_admin.register(User)
manager_admin.register(Group)
manager_admin.register(FormModel, FormModelAdmin)
manager_admin.register(FormModelData, FormModelDataAdmin)
manager_admin.register(project)


class ProjectAdmin(AdminSite):
    login_template = 'login.html'

project_admin = ProjectAdmin(name='projectadmin')
project_admin.register(FormModel, FormModelAdmin)
#project_admin.register(FormModelData, FormModelDataAdmin)
project_admin.register(project)
