
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _

from config.choice import RoleUser

# Create your models here.
class AccountUser(AbstractUser):
    role_user = models.CharField(_("Role User"), max_length=20, choices=RoleUser.choices, default=RoleUser.TAMU)
    

    
