from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
def index(request):

    template = loader.get_template('rango/index.html')
  
    context = RequestContext(request, {'boldmessage':'I am bold font from the context' } )
    return HttpResponse(template.render(context))


def about(request):
	template = loader.get_template('rango/about.html')
	context = RequestContext(request, {'italicmessage': 'I am italic from the context'})
	return HttpResponse(template.render(context))

	


