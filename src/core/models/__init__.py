# -*- coding: utf-8 -*-
from django.db.models import Model

from .public_ids import PublicIdModel
from .timestamped import TimeStampedModel


class BaseModel(TimeStampedModel, PublicIdModel, Model):
    """
    Base model to be used in the store application.
    """
    class Meta:
        abstract = True
        get_latest_by = 'created'
