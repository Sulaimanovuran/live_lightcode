from django.contrib import admin

from webapp.models import User, Leads, Course, EducationalMaterials, Profile

admin.site.register(User)
admin.site.register(Leads)
admin.site.register(Course)
admin.site.register(EducationalMaterials)
admin.site.register(Profile)
