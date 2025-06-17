from django import forms
from .models import ThriftItem

class ThriftItemForm(forms.ModelForm):
    class Meta:
        model = ThriftItem
        fields = ['name', 'description', 'price','image']