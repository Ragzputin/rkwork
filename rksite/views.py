###################################################
#RAGHAV KUMAR'S PERSONAL WEBSITE: raghavkumar.work#
#Date Started: January 18, 2015                   #
###################################################

from django.template import RequestContext
from django.shortcuts import render_to_response

def index(request):
    context = RequestContext(request)
    contex_dict = {'summary': 'Raghav Kumar\'s Summary goes here'}
    return render_to_response('rksite/index.html', contex_dict, context)

def contact(request):
    context = RequestContext(request)
    contex_dict = {'cinfo': 'Please contact at 226-220-3555'}
    return render_to_response('rksite/index.html', contex_dict, context)