from django.db import models
import django

# Create your models here.
class LocationModel():
    """Model for testing data"""
    id = models.AutoField(primary_key=True)
    amount = models.BigIntegerField()
    is_free_trial = models.BooleanField(default=False)
    duration = models.CharField(max_length=100,blank=True,unique=False)
    created_at = models.DateTimeField(default=django.utils.timezone.now, blank=True)
    updated_at = models.DateTimeField(default=django.utils.timezone.now, blank=True)
    objects = models.Manager()

mainClassNameWithModel = 'LocationModel'
