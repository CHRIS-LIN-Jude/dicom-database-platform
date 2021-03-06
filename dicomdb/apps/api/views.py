'''
Copyright (c) 2017 Vanessa Sochat

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

'''


from django.http import (
    Http404, 
    JsonResponse, 
    HttpResponse
)

from django.template import RequestContext
from django.shortcuts import render, render_to_response
import hashlib

from dicomdb.settings import API_VERSION as APIVERSION
from dicomdb.apps.main.models import (
    Batch,
    Image,
    Header
)

from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from dicomdb.apps.api.serializers import (
    BatchSerializer,
    ImageSerializer,
    HeaderSerializer
)
from django.contrib.auth.models import User

#########################################################################
# GET
# requests for information about reports and collections
#########################################################################

def api_view(request,api_version=None):
    if api_version == None:
        api_version = APIVERSION
    context = {"api_version":api_version,
               "active":"api"}
    return render(request, 'routes/api.html', context)


class HeaderViewSet(viewsets.ReadOnlyModelViewSet):
    '''A header includes a field and value
    '''
    queryset = Header.objects.all()
    serializer_class = HeaderSerializer


class BatchViewSet(viewsets.ReadOnlyModelViewSet):
    '''A batch is a collection of images to be processed.
    '''
    queryset = Batch.objects.all().order_by('uid')
    serializer_class = BatchSerializer

class ImageViewSet(viewsets.ReadOnlyModelViewSet):
    '''An image is one dicom image (beloning to a batch) to process
    '''
    queryset = Image.objects.all().order_by('uid')
    serializer_class = ImageSerializer
