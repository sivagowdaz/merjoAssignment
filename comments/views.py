from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import JsonResponse
from rest_framework.response import Response
from .serializers import CommentSerializer
from rest_framework import viewsets
from .models import Comment
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework import status
from rest_framework.decorators import action
from blogs.models import BlogPost

class CommentViewSets(viewsets.ViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    
    def retrieve(self, request, pk=None):
        try:
            blog = BlogPost.objects.get(pk=pk)
            comments = blog.comments.all()
            serializer = CommentSerializer(comments, many=True)
            return Response({"message":serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message":str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
        
    def create(self, request):
        data = request.data
        print("user is", request.jwt_payload)
        try:
            user_id = request.jwt_payload.get('id')
            user = User.objects.get(pk=user_id)
            blog = BlogPost.objects.get(pk=data['blog_id'])

            comment = Comment(content=data['content'], auther=user)
            comment.save()

            blog.comments.add(comment)
            blog.save()
            return Response({"message":"success"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message":str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def update(self, request, pk=None):
        data = request.data
        try:
            user_id = request.jwt_payload.get('id')
            user = User.objects.get(pk=user_id)
            comment = Comment.objects.get(pk=pk)
            if not comment.auther == user:
                raise Exception("Permission denaied")
            if data.get('content', None):
                comment.content = data['content']
            comment.save()
            return Response({"message":"success"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message":str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def destroy(self, request, pk=None):
        try:
            user_id = request.jwt_payload.get('id')
            user = User.objects.get(pk=user_id)
            comment = Comment.objects.get(pk=pk)
            if not comment.auther == user:
                raise Exception("Permission denaied")
            comment.delete()
            return Response({"message":"success"}, status=status.HTTP_200_OK)
        except Exception as e:
             return Response({"message":str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    
