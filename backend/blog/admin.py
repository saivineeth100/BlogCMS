from django.contrib import admin
from blog.models import BlogPost,BlogPost_History

# Register your models here.

admin.site.register(BlogPost)
admin.site.register(BlogPost_History)
