from django.contrib import admin
from .models import FacultyCordinators,StudentCordinators,Devs
# Register your models here.
admin.site.register(FacultyCordinators)
admin.site.register(StudentCordinators)
admin.site.register(Devs)