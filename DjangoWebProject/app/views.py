﻿"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import generics, permissions
from app.serializer.serializer import UserSerializer, GroupSerializer, RelevanceSerializer
from app.models import Relevance
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view, permission_classes, parser_classes

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index_django.html',
        context_instance = RequestContext(request,
        {
            'title':'Home Page',
            'year':datetime.now().year,
        })
    )

def test(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        context_instance = RequestContext(request,
        {
            'title':'Home Page',
            'year':datetime.now().year,
        })
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        context_instance = RequestContext(request,
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        })
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        context_instance = RequestContext(request,
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        })
    )

@api_view(['GET', 'POST', 'PATCH'])
@permission_classes((permissions.AllowAny, ))
#@parser_classes((JSONParser,))
@csrf_exempt
def test_api(request):
    print('test_api hit')
    if request.method == 'GET':
        item1 = request.query_params['item1']
        item1 = request.query_params['item2']
        relevance_request = Relevance(item1 = item1, item2 = item1)
        relevance_request.save()
        serilizer = RelevanceSerializer(relevance_request)
    elif request.method == 'POST':
        if hasattr(request, 'stream'):
            #print(request.stream.read())
            print('start extract data')
            item1 = request.data.get('item1')
            item2 = request.data.get('item2')
            print(item1)
            print(item2)
            print(request.stream.read())
            relevance_request = Relevance(item1 = item1, item2 = item2)
            serilizer = RelevanceSerializer(relevance_request)
    elif request.method == 'PUT':
        pass
    return JSONResponse(serilizer.data)

@api_view(['GET', 'POST', 'PATCH'])
@permission_classes((permissions.AllowAny, ))
def caculate_relevance(request):
    if request.method == 'GET':
        relevance_request = Relevance(item1 = '111', item2 = '222')
        serilizer = RelevanceSerializer(relevance_request)
    elif request.method == 'POST':
        serilizer = RelevanceSerializer(data=request.data)
        if not serilizer.is_valid():
            return
        pass
    elif request.method == 'PUT':
        pass
    return JSONResponse(serilizer.data)

class JSONResponse(HttpResponse):
    def __init__(self, content = b'', *args, **kwargs):
        content = JSONRenderer().render(content)
        kwargs['content_type'] = 'application/json'
        return super(JSONResponse,self).__init__(content, *args, **kwargs)

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
