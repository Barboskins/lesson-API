import json

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

from post.models import Comment

# Create your views here.
from post.serializers import CommentSerializer



class CommentsView(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer



class CommentView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
