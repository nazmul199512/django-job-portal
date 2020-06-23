from django.contrib import admin
from .models import *

admin.site.register(Contact)
admin.site.register(JobListing)
admin.site.register(ApplyJob)


class JobListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'user')
    actions = None

    def save_model(self, request, obj, form, change):
        if not obj.user:
            obj.user = request.user
            obj.save()

