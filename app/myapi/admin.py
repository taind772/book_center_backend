from django.contrib import admin
from .models import Authors, Documents, Users, Majors, Subjects, Publishers

admin.site.register(Authors)
admin.site.register(Documents)
admin.site.register(Users)
admin.site.register(Majors)
admin.site.register(Subjects)
admin.site.register(Publishers)
