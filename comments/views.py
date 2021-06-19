from django.shortcuts import render
from rest_framework import generics
from .serializers import CommentsSerializer , ReplySerializer
from .models import Comments , Reply
from rest_framework.permissions import AllowAny


# adding new comment
class AddComment(generics.CreateAPIView):
    permission_classes = [AllowAny,]
    serializer_class = CommentsSerializer
    queryset = Comments.objects.all()


#updating any existing comment
class UpdateComment(generics.UpdateAPIView):
    permission_classes = [AllowAny,]
    serializer_class = CommentsSerializer
    queryset = Comments.objects.all()

#adding a reply 
class AddReply(generics.CreateAPIView):
    permission_classes = [AllowAny,]
    serializer_class = ReplySerializer
    queryset = Reply.objects.all()

#deleting a comment
class DeleteComment(generics.DestroyAPIView):
    permission_classes = [AllowAny,]
    serializer_class = CommentsSerializer
    queryset = Comments.objects.all()
  

#getting all comments
class AllComments(generics.ListAPIView):
    permission_classes = [AllowAny,]
    serializer_class = CommentsSerializer
    queryset = Comments.objects.all()
