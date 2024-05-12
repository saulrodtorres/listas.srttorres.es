from django.http import HttpResponse

def vista_home(request):
    return HttpResponse('Hola, soy la vista home')