from django.contrib import admin
from .models import Post

# Register your models here.
class DesignPostAdmin(admin.ModelAdmin):
    # create table 
    list_display = ["id","name","category","author","desc"]
    # pagination
    list_per_page = 3

    list_editable=["name"]

    list_filter = ["category","name"]

    search_fields=["name","category"]

    fields = ["author","category","name","desc"]

admin.site.register(Post,DesignPostAdmin)