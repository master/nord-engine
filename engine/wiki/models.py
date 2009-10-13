# -*- coding: utf-8 -*-
from datetime import datetime
from tagging.fields import TagField

from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from parser import wikify
from utils import *

class Page(models.Model):
    name = models.CharField(max_length=255)
    content = models.TextField()
    rendered = models.TextField()
    modified = models.DateTimeField(default=datetime.now)
    author = models.ForeignKey(User, null=True)
    tags = TagField()

    class Meta:
        ordering = ('name', )

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        wiki_root = reverse('wiki.views.dispatch')
        self.rendered = wikify(self.content, wiki_root)
        self.modified = datetime.now()
        super(Page, self).save(*args, **kwargs)

    def get_tag_list(self):
        return parse_tag_input(self.tags)

    def get_path(self):
        wiki_root = reverse('wiki.views.dispatch')
        return wiki_root + to_path(self.tags)
