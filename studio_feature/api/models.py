# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
""" Registry model with - 
    1. version - TODO- This ideally has to be a custom model field where 
    restricted characters are allowed.
    2. service - Name of the service - Char field
    3. change - Last change occured to this registry. By default - "created"
"""

class Registry(models.Model):
    service = models.CharField(max_length=100,blank=False, null=False)
    version = models.CharField(max_length=20, blank=False, null=False)
    change = models.CharField(max_length=100,blank=False,null=False,default="created")
    def __unicode__(self):
        return str(self.id)