"""
pdfshop models
"""

from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import FileField
from django.forms import forms
from django.utils.translation import ugettext_lazy as _
from magic import from_buffer


class Profile(models.Model):
    """
    Represents user profiles
    Has a one to one relation with auth.User
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    """
    Updates user profile
    First, it checks if user is created, then creates Profile or not
    Then it saves the instance
    """
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

class ContentTypeRestrictedFileField(FileField):
    """
    Same as FileField, but you can specify:
        * content_types - list containing allowed content_types
    """
    def __init__(self, *args, **kwargs):
        self.content_types = kwargs.pop("content_types", ['application/pdf'])

        super(ContentTypeRestrictedFileField, self).__init__(*args, **kwargs)

    def clean(self, *args, **kwargs):
        """Clean method"""
        data = super(ContentTypeRestrictedFileField, self).clean(*args, **kwargs)

        file = data.file
        #content_type = file.content_type
        content_type = from_buffer(file, mime=True)
        print(self.content_types, content_type)

        if not content_type in self.content_types:
            raise forms.ValidationError(_('Filetype not supported. Only PDF is allowed.'))

        return data

class PDF(models.Model):
    """Represents PDF files"""
    name = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    path = ContentTypeRestrictedFileField(upload_to='pdf', content_types=['application/pdf'])

class Text(models.Model):
    """Represents text files"""
    name = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    path = ContentTypeRestrictedFileField(upload_to='txt', content_types=['text/plain'])
