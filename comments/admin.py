from django.contrib import admin
from . import models

class CommentsModelAdmin(admin.ModelAdmin):

    class Meta:
        model = models.Comments
        fields = ('text','created_at')

class ReplyModelAdmin(admin.ModelAdmin):

    class Meta:
        model = models.Reply
        fields = "__all__"


# registering the models       
admin.site.register(models.Comments,CommentsModelAdmin)
admin.site.register(models.Reply,ReplyModelAdmin)
