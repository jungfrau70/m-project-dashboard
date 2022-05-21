from django.contrib import admin
from blog.models import Post

# Register your models here.
# Admin 사이트에 등록

#admin.site.register() 대신 데코레이터 사용
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'update_dt')
