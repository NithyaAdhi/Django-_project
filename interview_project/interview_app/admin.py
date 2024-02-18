from django.contrib import admin
from .models import School, Class, Student, Subject, Assessment_Areas, Awards, Summary, Answers

admin.site.register(School)
admin.site.register(Class)
admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(Assessment_Areas)
admin.site.register(Awards)
admin.site.register(Summary)
admin.site.register(Answers)