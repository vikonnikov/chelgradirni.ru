from django.contrib import admin
from core.models import Section, Keyword, Page, MenuItem

# Register your models here.

# class SectionAdmin(admin.ModelAdmin):
#     list_display = ('title', 'slug', 'position')
#     ordering =  ('position',)

class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'position')
    ordering =  ('position',)

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'url')
    ordering =  ('title',)

# admin.site.register(Section, SectionAdmin)

admin.site.register(Keyword)
admin.site.register(Page, PageAdmin)
admin.site.register(MenuItem, MenuItemAdmin)

