from django.db import models
from django.contrib.auth.models import User


class Practice(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=40)
    date = models.DateTimeField(auto_now_add=True)
    date_plan = models.DateTimeField()
    completed = models.BooleanField(default=False)

    class Meta:
        ordering = ('-date_plan',)

    def __str__(self):
        return f"{self.title}"


class Exercises(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    link = models.ForeignKey(Practice, blank=True, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    podhod = models.IntegerField()
    povtor = models.IntegerField()
    weight_work = models.IntegerField()
    completed = models.BooleanField(default=False)
    es = models.BooleanField(default=False)
    md = models.BooleanField(default=False)
    hd = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title}"
