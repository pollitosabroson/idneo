# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _

from core.models import BaseModel


class Category(BaseModel):
    """
    Model that categorys.
    """
    name = models.CharField(
        max_length=80,
        verbose_name=_('name')
    )

    def __unicode__(self):
        return '{0}'.format(self.name)


class Type(BaseModel):
    """
    Model that types.
    """
    name = models.CharField(
        max_length=80,
        verbose_name=_('name')
    )

    def __unicode__(self):
        return '{0}'.format(self.name)
