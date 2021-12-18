from django.db import models
from django.contrib.auth.models import User as auth_user


class CommentModel(models.Model):
    comment = models.CharField(max_length=240)
    author = models.ForeignKey(auth_user, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.author.username) + " " + str(self.comment)
