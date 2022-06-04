from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


from users.models import User


@admin.register(User)
class ClientAdmin(UserAdmin):
    def __init__(self, model, admin_site):
        super().__init__(model, admin_site)
