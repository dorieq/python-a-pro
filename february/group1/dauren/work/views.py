from django.http import HttpResponse

def v(request):
    return HttpResponse("abcd")