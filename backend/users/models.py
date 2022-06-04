from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser as BaseAbstractUser, Group, Permission

# custom base class for users


class AbstractUser(BaseAbstractUser):

    phone_number = models.CharField(max_length=13, null=True, blank=True)
    dp = models.URLField(null=True, blank=True)
    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        help_text=_(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        related_name="%(app_label)s_%(class)s_related",
        related_query_name="%(app_label)s_%(class)ss",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        help_text=_('Specific permissions for this user.'),
        related_name="%(app_label)s_%(class)s_related",
        related_query_name="%(app_label)s_%(class)ss",
    )

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.username}"


class UserRoles(models.TextChoices):
    SUPERADMIN = 'SAdmin', _('SuperAdmin')
    ADMIN = 'Admin', _('Admin')
    READER = 'Reader', _('Reader')


class User(AbstractUser):

    user_role = models.CharField(
        max_length=6, choices=UserRoles.choices, default=UserRoles.READER)

    class Meta:
        db_table = 'Users'
