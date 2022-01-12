from django.shortcuts import render
from django.conf import settings

def invalid_request(request):
    
    template = settings.TEMPLATE_PATH or 'RequestLimiter/403.html'
    if type(template) is dict:
        return render(request, template['path'], template['context'] if template['context'] else None)
    
    context = {
        'head': 'Requisição interceptada',
        'body': 'Foi detectado um número indevido de requisições em sua sessão. Por favor, aguarde um pouco e tente novamente...',
        'lang': settings.LANGUAGE_CODE
    }
    
    return render(request, template, context)

