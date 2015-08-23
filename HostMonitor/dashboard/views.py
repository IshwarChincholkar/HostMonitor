from django.shortcuts import RequestContext
from django.shortcuts import render_to_response


# Create your views here.
def home(request):
    my_context = "HELLO"
    return render_to_response('home.html',my_context,context_instance=RequestContext(request))