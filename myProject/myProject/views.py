from django.shortcuts import render,redirect

from django.http import HttpResponse,JsonResponse

from account.models import *

from account.serializers import *

from rest_framework.renderers import JSONRenderer

#single student data
def studentDetails(request,pk):
    
    student=Student_Model.objects.get(id=pk)
    
    stdSerializers=StudentSerializers(student)
    
    return JsonResponse (stdSerializers.data)

#All student data/Query Set
def studentList(request):
    
    student=Student_Model.objects.all()
    
    stdSerializers=StudentSerializers(student,many=True)
    
    json_data = JSONRenderer().render(stdSerializers.data)
    
    return HttpResponse(json_data,content_type='application/json')
    
    