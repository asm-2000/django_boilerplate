from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from global_models.SoftDeleteModel import BaseModel


class UserManager(BaseUserManager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)

    def get_by_natural_key(self, username):
        return self.get(username=username)

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(username, email, password, **extra_fields)

    def create_user(self, username, email, password=None, **extra_fields):
        if not username:
            raise ValueError("The Username field must be set")
        if not email:
            raise ValueError("The Email field must be set")

        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user


class User(BaseModel, AbstractUser):
    username = models.CharField(
        max_length=255, unique=True, db_column="USERNAME", blank=False
    )
    email = models.EmailField(unique=True, db_column="EMAIL", blank=False)
    sso_email = models.EmailField(db_column="SSO_EMAIL", blank=True)
    password = models.CharField(max_length=255, db_column="PASSWORD", blank=False)
    is_active = models.BooleanField(default=True, db_column="IS_ACTIVE")
    is_user = models.BooleanField(default=True, db_column="IS_USER")
    is_staff = models.BooleanField(default=False, db_column="IS_STAFF")
    is_superuser = models.BooleanField(default=False, db_column="IS_SUPERUSER")
    date_joined = models.DateTimeField(auto_now_add=True, db_column="DATE_JOINED")
    last_login = models.DateTimeField(null=True, db_column="LAST_LOGIN")
    created_at = None
    updated_at = None
    first_name = None
    last_name = None

    REQUIRED_FIELDS = ["email", "password"]
    EMAIL_FIELD = "username"
    objects = UserManager()

    class Meta:
        db_table = "USER"

    def __str__(self):
        return self.username

    def natural_key(self):
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
