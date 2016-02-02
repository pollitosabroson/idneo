# -*- coding: utf-8 -*-
from hashlib import md5, sha256

from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _

from catalogs.models import Category, Type
from core.models import BaseModel


def get_upload_path(instance, filename):
    """
    Returns the proper path to upload an ```BookVersion``` gallery image
    based in the public id of the instance.

    Example: 'books/1Ax5/d2b5ca33bd970f64a6301fa75ae2eb22.png'
    """
    return 'books/%s/%s.jpg' % (
        instance.book.public_id,
        md5(instance.book.public_id + filename).hexdigest()
    )


def get_upload_thumbnail_path(instance, filename):
    """

    Returns the proper path to upload an ```BookVersion thumbnail ``` gallery
    image based in the public id of the instance.

    Example: 'books/thumbnail/1Ax5/d2b5ca33bd970f64a6301fa75ae2eb22.png'
    """
    get_hash = md5(instance.book.public_id + filename).hexdigest()
    get_hash = 'thumb_' + get_hash
    return 'books/thumbnail/%s/%s.jpg' % (
        instance.book.public_id,
        get_hash
    )


def get_upload_archive_path(instance, filename):
    """
    Returns the proper path to upload an ```BookVersion``` gallery image
    based in the public id of the instance.
    """
    get_hash = sha256(str(instance.id) + filename).hexdigest()
    return 'book/{0}/version/{1}/{2}'.format(
        instance.book.public_id,
        instance.public_id,
        get_hash
    )


class Book(BaseModel):
    """
    Model that Books.
    """
    title = models.CharField(
        max_length=255,
        verbose_name=_('title')
    )
    description = models.TextField(
        verbose_name=_('description')
    )
    format = models.ForeignKey(
        Type,
        related_name='books',
        verbose_name=_('format')
    )
    category = models.ForeignKey(
        Category,
        related_name='books',
        verbose_name=_('format')
    )
    cover = models.ImageField(
        upload_to=get_upload_path,
        blank=True,
        null=True,
        verbose_name=_('cover book'),
        max_length=255,
    )
    thumbnail = models.ImageField(
        upload_to=get_upload_thumbnail_path,
        blank=True,
        null=True,
        verbose_name=_('cover book thumbnail'),
        max_length=255,
    )

    published_date = models.DateField(
        verbose_name=_('published date')
    )
    price = models.DecimalField(
        decimal_places=2,
        max_digits=6,
        verbose_name=_('price')
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name=_('is active')
    )

    archive = models.FileField(
        upload_to=get_upload_archive_path,
        verbose_name=_('archive'),
        max_length=255,
        blank=False,
        null=False,
    )

    @property
    def cover_url(self):
        try:
            return self.cover.url
        except:
            return settings.STATIC_URL + 'img/book-red.jpg'

    @property
    def thumbnail_url(self):
        try:
            return self.thumbnail.url
        except:
            return settings.STATIC_URL + 'img/book-red.jpg'

    def __unicode__(self):
        return '%s' % self.title
