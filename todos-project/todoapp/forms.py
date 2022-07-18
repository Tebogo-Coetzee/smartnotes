from dataclasses import fields
from statistics import mode
from django import forms

from .models import Mytodo

class TodoForm(forms.ModelForm):
    class Meta(object):
       model = Mytodo
       fields = ['task',]