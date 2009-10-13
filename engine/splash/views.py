from django.http import HttpResponse, HttpResponseRedirect

from random import choice, seed
from models import Image

def image(request):
    seed(request.META['REMOTE_ADDR'])
    image = choice(Image.objects.filter(enabled=True))
    return HttpResponseRedirect(image.path)

