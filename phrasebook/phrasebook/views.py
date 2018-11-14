from django.http import HttpResponse
from django.template import loader


def translator(request):
    template = loader.get_template('translator.html')
    return HttpResponse(template.render({}, request))