from django.urls import path

# External
from rest_framework_simplejwt.views import TokenRefreshView,TokenVerifyView

# Custom
from api.auth import views

urlpatterns = [
    path('login/', views.LoginView.as_view(),name="login"),
    path('refreshtoken/', TokenRefreshView.as_view(),name="refreshtoken"),
    path('verifytoken/', TokenVerifyView.as_view(),name="verifytoken"),

]
