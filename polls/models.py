# -*- coding: utf-8 -*-

from django.db import models

from cms.models import CMSPlugin

# existing Poll and Choice models...

class PollPluginModel(CMSPlugin):
    #poll = models.ForeignKey('polls.Poll', related_name='plugins')
    name = models.CharField(max_length=32)

    def __unicode__(self):
      return self.name