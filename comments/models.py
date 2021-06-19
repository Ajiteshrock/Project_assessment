from django.db import models


class Comments(models.Model):
    title_for_comment = models.CharField(max_length=200,default="")
    text = models.TextField(max_length=3000,default="",blank=False)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title_for_comment

class Reply(models.Model):
    reply_text = models.TextField(max_length=2000,default="",blank=False)
    created_at = models.DateField(auto_now_add=True)
    comment = models.ForeignKey(Comments, on_delete=models.CASCADE,related_name='reply')

    def __str__(self):
        return self.reply_text[:40]+"..."
