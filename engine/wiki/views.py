from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.utils.http import urlquote
from forms import PageForm
from models import Page
from tagging.models import Tag, TaggedItem


def edit(request, name):
    if not request.user.is_authenticated():
        raise Http404

    page = get(Page, name, True)

    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            if not page:
                page = Page()
            page.name = form.cleaned_data['name']
            page.content = form.cleaned_data['content']
            page.author = request.user
            page.tags = ' '.join(filter(None, name.split('/')))
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

    page = get(Page, name, True)

    if page:
        page.delete()
    else:
        raise Http404
    return HttpResponseRedirect('%s' % urlquote(name))


def view(request, name):
    if name == '':
        name = 'index'

    page = get(Page, name, True)
    pages = [page] if page else get(Page, name)

    if len(pages) == 0 and not request.user.is_authenticated():
        raise Http404

    return render_to_response('view.html', {'pages': pages,
                                            'name': name,
                                            'user': request.user})


def get(model, name, precise=False):
    tags = ' '.join(filter(None, name.split('/')))
    objects = TaggedItem.objects.get_by_model(model, tags)
    tag_set = str_to_set(tags)
    if precise:
        items = filter(lambda i: str_to_set(i.tags) == tag_set, objects)
        return items.pop() if len(items) == 1 else None
    else:
        return filter(lambda i: str_to_set(i.tags) >= tag_set, objects)


def str_to_set(s):
    return set(s.split(' '))
