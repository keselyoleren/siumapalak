from django.db.models import TextChoices

class RoleUser(TextChoices):
    ADMIN = 'admin'
    DEVELOPER = 'developer'