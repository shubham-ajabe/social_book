from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class User(AbstractUser):
    groups = models.ManyToManyField(Group, related_name='accounts_user_set')
    user_permissions = models.ManyToManyField(Permission, related_name='accounts_user_permissions_set')