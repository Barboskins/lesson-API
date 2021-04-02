import json

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from post.models import Comment

# Create your views here.

def comments_view(request):
    if request.method not in ['GET','POST']:
        return HttpResponse (status=405)
    if request.method == 'GET':
        comments =[{'id':c.id,'author':c.author, 'text':c.text} for c in Comment.objects.all()]
        return JsonResponse(comments, safe = False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        c = Comment.objects.create(**data)
    return JsonResponse({'id':c.id,'author':c.author, 'text':c.text}, status=201)

def comment_view(request):
    pass
