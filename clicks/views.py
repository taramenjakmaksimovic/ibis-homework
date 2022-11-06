from django.http import HttpResponse
from clicks.models import Clicks
from datetime import datetime


def number_of_clicks(request, campaign):
    if request.GET.get('startdate') and request.GET.get('enddate'):
        date1 = request.GET.get('startdate')
        date2 = request.GET.get('enddate')
        try:
            t1 = datetime.strptime(date1, "%Y-%m-%d %H:%M:%S")
            t2 = datetime.strptime(date2, "%Y-%m-%d %H:%M:%S")
        except ValueError:
            return HttpResponse('At least one of the dates is in incorrect format. Expected format is '
                                '"yyyy-mm-dd hh:mm:ss".Try again.', status=400)

        unix1 = t1.timestamp()
        unix2 = t2.timestamp()
        return HttpResponse(Clicks.objects.filter(campaign=campaign, timestamp__range=[unix1, unix2]).count())
    else:
        return HttpResponse(Clicks.objects.filter(campaign=campaign).count())
