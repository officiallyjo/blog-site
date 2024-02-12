from django.contrib import admin

from .models import Post,Tag,Author


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_filter =("Author","Tag","Date",)
    list_display= ("Title","Date","Author",)
    prepopulated_fields ={"Slug":("Title",)}

admin.site.register(Post,PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)


