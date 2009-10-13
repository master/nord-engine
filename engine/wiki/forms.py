# -*- coding: utf-8 -*-
from django import forms as forms
from models import Page

class PageForm(forms.Form):
    name = forms.CharField(max_length=255)
    content = forms.CharField(widget=forms.Textarea())
