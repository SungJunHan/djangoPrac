from django.db import models


class VideosName(models.Model):

    title = models.CharField(max_length=200)
    body = models.CharField(max_length=200)
    uploadDate = models.DateTimeField('date published')
    replyCnt = models.IntegerField(default=0)


class Reply(models.Model):
    title = models.ForeignKey(VideosName, on_delete=models.CASCADE)
    replyBody = models.CharField(max_length=100)
    writer = models.CharField(max_length=100)





