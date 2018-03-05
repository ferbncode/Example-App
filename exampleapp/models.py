from django.db import models
from django.utils import timezone
from django.urls import reverse


class ParentInfograph(models.Model):
    pid = models.AutoField('pid', primary_key=True)
    name = models.CharField(max_length = 100, blank=False, null=False, unique=True)
    description = models.CharField(max_length = 255, blank=False, null=False)
    datecreated = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "ParentInfograph"
        verbose_name_plural = "ParentInfographs"
        ordering = ['datecreated', ]


class InfographCategory(models.Model):
    pid = models.PositiveIntegerField(primary_key=True,unique=True)
    category = models.CharField(max_length = 30)

    class Meta:
        verbose_name = "InfographCategory"
        verbose_name_plural = "InfographCategories"

class Infograph(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    pid = models.PositiveIntegerField()
    name = models.CharField(max_length = 100)
    description = models.CharField(max_length = 255)
    date_created = models.DateTimeField(default=timezone.now)
    cid = models.PositiveIntegerField()
    statusID = models.PositiveIntegerField()
    sourceID = models.PositiveIntegerField()
    # One to Many Relationship
    parentinfograph = models.ForeignKey(ParentInfograph, on_delete=models.CASCADE)

    # Zero to Many Relationship
    infograph_category = models.ForeignKey(InfographCategory, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Infograph"
        verbose_name_plural = "Infographs"
        ordering = ['date_created', ]


class Topic(models.Model):
    tid = models.PositiveIntegerField(primary_key=True)
    mtid = models.PositiveIntegerField(primary_key=False)
    topic_code = models.CharField(max_length = 50)
    topicdescription = models.CharField(max_length = 50)

    class Meta:
        verbose_name = "Topic"
        verbose_name_plural = "Topics"


class InfographAssociations(models.Model):
    iad = models.PositiveIntegerField(primary_key=True)
    iid = models.PositiveIntegerField()
    tid = models.PositiveIntegerField()
    mtgid = models.PositiveIntegerField()
    eid = models.PositiveIntegerField()
    gpid = models.PositiveIntegerField()
    datecreated = models.DateTimeField(default=timezone.now)
    statusid = models.PositiveIntegerField()
    inforgraph = models.ForeignKey(Infograph, on_delete=models.CASCADE, blank=True, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, blank=True, null=True)


