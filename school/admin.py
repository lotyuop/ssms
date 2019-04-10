from django.contrib import admin
from school.models import State, Lga, SchoolClass, SubClass, Bloodgroup

# Register your models here.
admin.site.register(State)
admin.site.register(Lga)
admin.site.register(SchoolClass)
admin.site.register(SubClass)
admin.site.register(Bloodgroup)