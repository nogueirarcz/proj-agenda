from django.contrib import admin
from app_contact.models import Contact

# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):

    list_display = ('id', 'first_name', 'last_name', 'phone',)
    
    ordering = ('-id',)

    list_filter = ('created_date',)

    search_fields = ('first_name', 'second_name',)

    list_per_page = 10

    list_max_show_all = 100

    list_display_links = ('id', 'first_name',)
