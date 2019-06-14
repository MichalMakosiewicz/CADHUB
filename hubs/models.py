from django.db import models


class Project(models.Model):
    project_title = models.CharField(max_length=50)
    start_date = models.DateTimeField("date of project start.")


class Activation(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)