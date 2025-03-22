from django.db import models
from django.contrib.auth.models import AbstractUser
from global_models.SoftDeleteModel import BaseModel


class User(BaseModel, AbstractUser):
    username = models.CharField(
        max_length=255, unique=True, db_column="USERNAME", blank=False
    )
    email = models.EmailField(unique=True, db_column="EMAIL", blank=False)
    sso_email = models.EmailField(unique=True, db_column="SSO_EMAIL", blank=True)
    password = models.CharField(max_length=255, db_column="PASSWORD", blank=False)
    is_active = models.BooleanField(default=True, db_column="IS_ACTIVE")
    is_user = models.BooleanField(default=True, db_column="IS_USER")
    is_staff = models.BooleanField(default=False, db_column="IS_STAFF")
    is_superuser = models.BooleanField(default=False, db_column="IS_SUPERUSER")
    date_joined = models.DateTimeField(auto_now_add=True, db_column="DATE_JOINED")
    last_login = models.DateTimeField(null=True, db_column="LAST_LOGIN")
    created_at = None
    updated_at = None
    first_name = models.CharField(max_length=255, db_column="FIRST_NAME", blank=False)
    last_name = models.CharField(max_length=255, db_column="LAST_NAME", blank=False)

    REQUIRED_FIELDS = ["email", "password"]
    EMAIL_FIELD = "username"

    class Meta:
        db_table = "USER"

    def __str__(self):
        return self.username


class UserDetails(BaseModel):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="user_details", db_column="USER_ID"
    )
    first_name = models.CharField(max_length=255, db_column="FIRST_NAME", blank=False)
    last_name = models.CharField(max_length=255, db_column="LAST_NAME", blank=False)
    profile_image_url = models.CharField(
        max_length=255, db_column="PROFILE_IMAGE_URL", blank=True
    )
    date_of_birth = models.DateField(db_column="DATE_OF_BIRTH", blank=True)
    country = models.CharField(max_length=255, db_column="COUNTRY", blank=True)

    class Meta:
        db_table = "USER_DETAILS"
