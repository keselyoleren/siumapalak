from django.db.models import TextChoices

class RoleUser(TextChoices):
    TAMU = 'tamu'
    OPERATOR = 'operator'
    ADMIN = 'admin'