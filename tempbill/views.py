from django.template import loader
from django.http import HttpResponse

from .models import Bill


def index(request):
    bill_list = Bill.objects.order_by('-bill_time')
    template = loader.get_template('tempbill/index.html')
    return HttpResponse(template.render({'bill_list':bill_list}, request));


def bill(request, bill_id):
    pass


def medicine(request):
    pass
