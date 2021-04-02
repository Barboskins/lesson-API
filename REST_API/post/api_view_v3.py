import json

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from post.models import Comment

# Create your views here.
from post.serializers import CommentSerializer



class CommentsView(APIView):
    def get(self, request, *args, **kwargs):
        s = CommentSerializer(Comment.objects.all(), many=True)
        return Response(s.data)

    def post(self, request, *args, **kwargs):
        s = CommentSerializer(data=request.data)
        s.is_valid(raise_exception=True)
        c = Comment.objects.create(**s.validated_data)
        return Response(CommentSerializer(c).data, status=status.HTTP_201_CREATED)









def comment_view(request):
    pass