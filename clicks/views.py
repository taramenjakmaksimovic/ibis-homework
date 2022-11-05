from django.http import HttpResponse
from clicks.models import Clicks


def index(request, campaign):
    return HttpResponse(Clicks.objects.filter(campaign=campaign).count())

