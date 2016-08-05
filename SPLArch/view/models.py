from django.db import models
from SPLArch.component.models import *

# Create your models here.

class ViewPoint(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    stakeholder = models.CharField(max_length=100)
    concern = models.CharField(max_length=100)
    componentOne = models.OneToOneField(Components, related_name='ComponentOne')
    componentTwo = models.OneToOneField(Components, related_name='ComponentTwo')
    relationship = models.CharField(max_length=100)
    property = models.CharField(max_length=100)
    restriction = models.CharField(max_length=100)
    viewPointRelated = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'View Point Item'
        verbose_name_plural = 'View Point'



    def __unicode__(self):
        return self.name

class View (models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    stakeholder = models.CharField(max_length=100)
    concern = models.CharField(max_length=100)
    diagram = models.CharField(max_length=100)
    viewPointRelated = models.ManyToManyField(ViewPoint)
    variabilityGuidelines = models.ManyToManyField(VariabilityGuidelines, related_name='Variability View')

    class Meta:
        verbose_name = 'View Item'
        verbose_name_plural = 'View'

    def __unicode__(self):
        return self.name

class StructuralVision (models.Model):
    presentation = models.CharField(max_length=200)
    architectureStyle = models.CharField(max_length=200)
    modelDiagram = models.CharField(max_length=100)
    model = models.ManyToManyField(Module)
    viewPointRelated = models.ManyToManyField(ViewPoint)
    variabilityGuidelines = models.ManyToManyField(VariabilityGuidelines, related_name='Variability Structural')

    class Meta:
        verbose_name = 'Structural Vision Item'
        verbose_name_plural = 'Structural Vision'

    def __unicode__(self):
        return self.presentation

class BehaviorVision (models.Model):
    diagram = models.CharField(max_length=100)
    featuresRelated = models.ManyToManyField(Feature, related_name='Feature Behavior')
    sequenceDiagram = models.CharField(max_length=100)
    viewPointRelated = models.ManyToManyField(ViewPoint)
    variabilityGuidelines = models.ManyToManyField(VariabilityGuidelines, related_name='Variability Behavior')

    class Meta:
        verbose_name = 'Behavior Vision Item'
        verbose_name_plural = 'Behavior Vision'


