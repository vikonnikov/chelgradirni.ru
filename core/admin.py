from django.contrib import admin
from core.models import Section, Keyword, Page, MenuItem

# Register your models here.

class SectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'position')
    ordering =  ('position',)

admin.site.register(Section, SectionAdmin)

admin.site.register(Keyword)
admin.site.register(Page)
admin.site.register(MenuItem)

