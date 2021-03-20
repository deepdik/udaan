import datetime

from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _


class Store(models.Model):
    """
    """
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT, related_name='store')
    store_name = models.CharField(_('store name'), max_length=100)
    address = models.CharField(_('address'),
        max_length=300)
    slug = models.CharField(max_length=200, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'store'
        permissions = ()


def create_slug(instance, new_slug=None):
    """
    Method to create slug from shop name
    """
    slug = slugify(instance.store_name)
    if new_slug is not None:
        slug = new_slug
    qs = Store.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(pre_save_post_receiver, sender=Store)
