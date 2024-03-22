from django.http import HttpResponse

def homepage(request):
    return HttpResponse('<center>This is the Cargo application</center>')

