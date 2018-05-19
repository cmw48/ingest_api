from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from papers.models import Paper
from papers.serializers import PaperSerializer

@csrf_exempt
def paper_list(request):
    """
    List all code papers, or create a new paper.
    """
    if request.method == 'GET':
        papers = Paper.objects.all()
        serializer = PaperSerializer(papers, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PaperSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def paper_detail(request, pk):
    """
    Retrieve, update or delete a code paper.
    """
    try:
        paper = Paper.objects.get(pk=pk)
    except Paper.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = PaperSerializer(paper)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = PaperSerializer(paper, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        paper.delete()
        return HttpResponse(status=204)
