from django import forms
from iot.models import Datapoint

class DatapointForm(forms.ModelForm):
   class Meta:
       model=Datapoint
       fields = '__all__'
       # fields = ['sensor', 'value', 'time']
