from django.contrib import admin
from app.models import *
# Register your models here.





# Admin Customizations 

class topicadmin(admin.ModelAdmin):
    list_display = ['topicname']


class webadmin(admin.ModelAdmin):
    # list_display_links and list_editable shouldn't contain same fields as links shoudn't be editable
    
    # Column that you want to display on admin page
    list_display = ['topicname','name','url']

    # TO display it in hyperlink format 
    list_display_links = ['url','name']

    # Allow you to edit and save
    #list_editable = ['email']

    # No.of records/rows displayed per page
    list_per_page = 1

    # Search Box 
    search_fields = ['name']

    # Filter colums --> Columns 
    # to display with values in sorted order
    list_filter = ['url','email']




admin.site.register(Topic,topicadmin)

admin.site.register(Webpage,webadmin)

admin.site.register(AccessRecord)

admin.site.site_title = 'WEBPAGE'

admin.site.site_header = 'My Models'


# Index_title changing --> By default Site Registrations
admin.site.index_title = 'Model Registrations' 




