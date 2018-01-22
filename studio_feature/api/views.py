# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from api.models import Registry
from api.serializer import RegistrySerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# Create your views here.

"""
Write API to create a new service in the registry
"""
@api_view(['POST'])
def create_service(request,format=None):
    
    serializer = RegistrySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        data={'change':'created'}
        return Response(data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

"""
Fetch a service from the registry
"""
@api_view(['GET'])
def get_service(request,format=None):
    
    params = request.query_params
    service = params.get('service')
    qfilter={}
    try:
        # if version is also provided as part of the search
        if 'version' in params:
            qfilter['version'] = params['version']
            services = Registry.objects.filter(service=service).filter(**qfilter)
            count = services.count()
        # if version is NOT provided as part of the search
        else:
            services = Registry.objects.filter(service=service)
            count = services.count()
    # Non-existing service. Hence return count as 0        
    except Registry.DoesNotExist:
        count = 0
    data = Registry.objects.all()
    services = RegistrySerializer(services,many=True)
    content={'count':count,'services':services.data}
    return Response(content)

"""
Updating a service
TODO - extend to update multiple records
- to enable version updates
- ask confirmation whether to update or not
"""
@api_view(['PUT'])
def update_service(request,pk,format=None):

    try:
        record = Registry.objects.get(pk=pk)
    except Registry.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    print request.data
    serializer = RegistrySerializer(record,data=request.data,partial=True)
    if serializer.is_valid():
        serializer.save()
        data={'change':'changed'}
        return Response(data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

"""
Removing a service
TODO find a better way to handle delete request - change version
- ask confirmation whether to delete or not
"""
@api_view(['POST'])
def delete_service(request,service):
    services = Registry.objects.filter(service=service)
    services.delete()
    data={'change':'removed'}
    return Response(data)