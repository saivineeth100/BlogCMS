
from django.shortcuts import render


from api.views import CRUDAPIView,ListSingleModelMixin
from blog.models import BlogPost_History
from users.models import UserRoles
from blog.models import BlogPost
from blog.serializer import BlogPostSerializer,BlogPost_ReviewSerializer
from users.models import UserRoles
from blog.models import BlogStatuses


class BlogCRUDAPIView(CRUDAPIView):
    lookup_field = "id"
    serializer_class = BlogPostSerializer
    model = BlogPost

    def create(self, request, *args, **kwargs):
        self.usertype = self.request.user.user_role 
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):        
        self.usertype = self.request.user.user_role 
        if(self.usertype == UserRoles.ADMIN):
            self.serializer_class = BlogPost_ReviewSerializer
            return self.create(request, *args, **kwargs)
        return super().update(request, *args, **kwargs)
    def perform_create(self, serializer):
        newargs = {"author":self.request.user}
        if(self.usertype == UserRoles.ADMIN and self.kwargs.get("id")):
            newargs["basepost_id"] = self.kwargs.get("id")              
        serializer.save(**newargs)

class BlogLIstAPIView(ListSingleModelMixin):
    permission_classes = []
    serializer_class = BlogPostSerializer
    model = BlogPost

    def get_queryset(self):
        return self.model.published.all()
