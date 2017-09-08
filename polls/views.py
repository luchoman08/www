# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from django.template import loader
""""
Define un ejemplo en el que se renderiza una lista de productos
""""
def ejemplo(request):
    template = loader.get_template('polls/ejemplo.html')
    alerts=[]
    for i in range (0,22):
        alerts.append('Agotado. Quitar de la lista producto ' + str(i) + '?')
    context ={
        'alerts': alerts,
        'panel_title': 'Reloj',
    }
    return HttpResponse(template.render(context, request)) 

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
