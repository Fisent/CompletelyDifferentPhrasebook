from django.http import HttpResponse, JsonResponse
from django.template import loader

from .glosbe_access import Glosbe


def translator(request):
    template = loader.get_template('translator.html')
    text = 'shoe word'

    glosbe = Glosbe(from_lang='eng', dest_lang='pol')

    tab = []

    for word in text.split():
        tab.append({'org': word,
                    'translated': glosbe.translate(word)[0]})

    context = {'text': tab}
    return HttpResponse(template.render(context, request))


def translate_word(request):
    glosbe = Glosbe(from_lang='eng', dest_lang='pol')
    translated = glosbe.translate(request.GET.get('word'))

    return JsonResponse({'translated': translated})
