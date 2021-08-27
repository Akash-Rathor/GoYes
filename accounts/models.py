from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta
# Create your models here.
class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    delete_at = models.DateTimeField(default=datetime.now()+timedelta(days=30))

    class Meta:
        abstract = True


# class ShortUrls(TimeStampMixin):
#     user_id = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
#     url = models.URLField(null=False,db_index=True)
#     ShortUrl = models.URLField(null=False,db_index=True)