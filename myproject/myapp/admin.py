from django.contrib import admin
from .models import Client

class ClientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone_number', 'address', 'date_of_birth', 'created_at', 'updated_at')
    search_fields = ('first_name', 'last_name', 'email', 'phone_number', 'address')

admin.site.register(Client, ClientAdmin)