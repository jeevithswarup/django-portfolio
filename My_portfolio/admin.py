from django.contrib import admin
from .models import *;

# admin.site.register(Projects)
admin.site.register(Skills)
admin.site.register(Contact)
admin.site.register(AcademicQualification)
admin.site.register(Certificates)
admin.site.register(Semester)
@admin.register(Intro)
class Introadmin(admin.ModelAdmin):
     def has_add_permission(self, request):
        if Intro.objects.exists():
            return False
        return True


class KeyFeatureInline(admin.TabularInline):
    model = KeyFeature
    extra = 6   # shows 6 empty boxes by default

@admin.register(Projects)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title',)
    inlines = [KeyFeatureInline]
admin.site.register(SocialMediaLink)     