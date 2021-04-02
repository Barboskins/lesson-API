import json

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from post.models import Comment

# Create your views here.
from post.serializers import CommentSerializer


@api_view(http_method_names=['GET', 'POST'])
def comments_view(request):
    if request.method == 'GET':
        s = CommentSerializer(Comment.objects.all(), many=True)
        return Response(s.data)

    elif request.method == 'POST':
        s = CommentSerializer(data=request.data)
        s.is_valid(raise_exception=True)
        c = Comment.objects.create(**s.validated_data)
        return Response(CommentSerializer(c).data, status=status.HTTP_201_CREATED)


def comment_view(request):
    pass