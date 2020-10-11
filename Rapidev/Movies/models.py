from django.db import models


class MoviesData(models.Model):
    name = models.CharField(max_length=20, default="")
    description = models.TextField(default="")
    imgPath = models.ImageField(upload_to="iamges/", default="")
    duration = models.IntegerField(default=0)
    genre = models.CharField(max_length=50, default="")
    language = models.CharField(max_length=20, default="")
    userRating = models.IntegerField(default=0)


class MpaaRating(models.Model):
    type = models.CharField(max_length=20, default="")
    label = models.CharField(max_length=20, default="")
    mdata = models.ForeignKey(MoviesData, on_delete=models.CASCADE)
