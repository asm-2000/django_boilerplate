from django_softdelete.models import SoftDeleteModel
from django.db import models
import uuid

class BaseModel(SoftDeleteModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_column="ID")
    created_at = models.DateTimeField(auto_now_add=True, db_column="CREATED_AT")
    updated_at = models.DateTimeField(auto_now=True, db_column="UPDATED_AT")
    is_deleted = models.BooleanField(default=False, db_column="IS_DELETED")
    deleted_at = models.DateTimeField(null=True, blank=True, db_column="DELETED_AT")
    restored_at = None
    transaction_id = None

    class Meta:
        abstract = True
    