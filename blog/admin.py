from django.contrib import admin
from blog.models import Post,Category


class PostAdmin(admin.ModelAdmin):
    list_display=('id','title','status')
    ordering=['id']
class CategoryAdmin(admin.ModelAdmin):
    list_display=('name',)
    ordering=['id']



admin.site.register(Category,CategoryAdmin)
admin.site.register(Post,PostAdmin)
