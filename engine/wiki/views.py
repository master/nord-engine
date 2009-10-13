# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.utils.http import urlquote

from forms import PageForm
from models import Page
from utils import *

from tagging.models import Tag, TaggedItem

def index(request, name):
    pages = get_subset_by_model(Page, to_tags(name))
    return render_to_response('index.html', {'pages': pages, 'path': name})

def view(request, name):
    page = get_set_by_model(Page, to_tags(name))
    if len(page) != 0:
        page = page[0]
    else:
        page = Page(name=name)

    return render_to_response('view.html', {'page': page, 'user': request.user})

def edit(request, name):
    if not request.user.is_authenticated():
        raise Http404

    page = get_set_by_model(Page, to_tags(name))
    if len(page) != 0:
        page = page[0]
    else:
        page = None
       
    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            if not page:
                page = Page()
            page.name = form.cleaned_data['name']
            page.content = form.cleaned_data['content']
            page.author = request.user
            page.tags = to_tags(name)
            page.save()
            return HttpResponseRedirect('%s' % urlquote(page.get_path()))
    else:
        if page:
            form = PageForm(initial=page.__dict__)
        else:
            form = PageForm(initial={'name': name})
    return render_to_response('edit.html', {'form': form})

def delete(request, name):
    if not request.user.is_authenticated():
        raise Http404

    page = get_set_by_model(Page, to_tags(name))
    if len(page) != 0:
        page = page[0]
    else:
        raise Http404

    path = page.get_path()
    page.delete()

    return HttpResponseRedirect('%s' % urlquote(path))

def dispatch(request, name):
    if name == '':
        name = 'index'

    page = get_set_by_model(Page, to_tags(name))
    if len(page) == 1:
        return view(request, name)
    else:
        if not request.user.is_authenticated():
            raise Http404
        else:
            pages = get_subset_by_model(Page, to_tags(name))
            if len(pages) == 0:
                return view(request, name)
            else:
                return index(request, name)
