from django.urls import path , include
from . import views

urlpatterns = [
    path('allcomments',views.AllComments.as_view(),name='All-comments'),
    path('addnew/',views.AddComment.as_view(),name='adding_comment'),
    path('editcomment/<int:pk>',views.UpdateComment.as_view(),name='edit-comment'),
    path('deletecomment/<int:pk>',views.DeleteComment.as_view(),name='add_reply'),
    path('addreply/',views.AddReply.as_view(),name='add_reply'),
]  