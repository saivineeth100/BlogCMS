from django.urls import path,include

from blog.views import BlogLIstAPIView,BlogCRUDAPIView

urlpatterns = [
    path('posts/', BlogCRUDAPIView.as_view(),name="blogcrud"),
    path('posts/<int:id>/', BlogCRUDAPIView.as_view(),name="blogcrud"),
    path('posts/all/', BlogLIstAPIView.as_view(),name="blogpostslist"),
    
]
