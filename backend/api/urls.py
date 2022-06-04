from django.urls import path,include

from api.auth import urls as APIAuthUrls

urlpatterns = [
    path('auth/', include(APIAuthUrls.urlpatterns)),
    path('blog/',include("blog.urls"))
]
