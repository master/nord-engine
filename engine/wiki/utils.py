# -*- coding: utf-8 -*-

from tagging.models import Tag, TaggedItem

def to_tags(s):
    return ' '.join(filter(None, s.split('/')))

def to_path(s):
    return '/'.join(filter(None, s.split(' ')))    

def str_to_set(s):
    return set(s.split(' '))

def get_subset_by_model(model, tags):
    tags_set = str_to_set(tags)
    return filter(lambda i: str_to_set(i.tags).issuperset(tags_set),
                  TaggedItem.objects.get_by_model(model, tags))

def get_set_by_model(model, tags):
    tags_set = str_to_set(tags)
    return filter(lambda i: str_to_set(i.tags) == tags_set,
                  TaggedItem.objects.get_by_model(model, tags))
