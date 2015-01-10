from django.contrib import admin
from core.models import Section

# Register your models here.

class SectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'position')
    ordering =  ('position',)

admin.site.register(Section, SectionAdmin)

