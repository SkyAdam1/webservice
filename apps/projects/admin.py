from django.contrib import admin
from .models import NiokrCriteria, NiokrProject, NiokrUser, Project, Criteria, Equipment

admin.site.register(Project)
admin.site.register(Equipment)
admin.site.register(Criteria)
admin.site.register(NiokrProject)
admin.site.register(NiokrCriteria)
admin.site.register(NiokrUser)
