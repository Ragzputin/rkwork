###################################################
#RAGHAV KUMAR'S PERSONAL WEBSITE: raghavkumar.work#
#Date Started: January 18, 2015                   #
###################################################

from django.template import RequestContext
from django.shortcuts import render_to_response
from rksite.forms import EmailForm
from rksite.models import Message
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from smtplib import SMTP

def index(request):
    context = RequestContext(request)
    contex_dict = {
                   'summary2': 'Sometimes he is simply a selfie in a car..',
                   'summary3': 'Sometimes you\'ll find him with a guitar..',
                   'summary4': 'And every now and then he stays at a place like this..nice right?',
                   'summary5': 'But only sometimes. Even Mexico can get expensive!',
                   'summary6': 'Besides all these shenanigans, Raghav Kumar is a recent alumnus of the University \
                               of Waterloo. That\'s pretty cool too right?',
                   'summary7': 'Look at that smile and thumbs up. This guy deserves at least an interview.',
                   }
    return render_to_response('rksite/index.html', contex_dict, context)

def projects(request):
    context = RequestContext(request)
    return render_to_response('rksite/projects.html', {}, context)

def goals(request):
    context = RequestContext(request)
    return render_to_response('rksite/goals.html', {}, context)

def contact(request):
    context = RequestContext(request)

    if request.method == 'POST':
        form = EmailForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            recipients = ['ray.kumar91@gmail.com']
            if email:
                message = 'Subject: ' + subject + '\n' + 'Contact: ' + name + ' - ' + email + '\n' + 'Message: ' \
                          + message

            send_mail(subject,message,email,recipients)
            return HttpResponseRedirect('/home/thanks/')
    else:
        form = EmailForm()

    return render_to_response('rksite/contact.html',{'form': form},context)

def thanks(request):
    context = RequestContext(request)
    context_dict = {}

    return render_to_response('rksite/thanks.html', context_dict, context)