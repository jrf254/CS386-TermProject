from django.contrib import admin
from django.contrib.admin import AdminSite
from .models import *

admin.site.register(project)
class ManagerAdmin(AdminSite):
    login_template = 'login.html'

manager_admin = ManagerAdmin(name='manageradmin')
manager_admin.register(User)
manager_admin.register(Group)
manager_admin.register(FormModel)
manager_admin.register(project)
manager_admin.register(FormModelData)

class ProjectAdmin(AdminSite):
    print AdminSite
    login_template = 'login.html'

#    index_template = 'admin_base.html'

project_admin = ProjectAdmin(name='projectadmin')
project_admin.register(FormModel)
project_admin.register(project)