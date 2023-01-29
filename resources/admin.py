from django.contrib import admin
from .models import Resource, AdditionalResource

# Register your models here.
admin.site.register(Resource)
admin.site.register(AdditionalResource)
