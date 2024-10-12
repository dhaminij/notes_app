from django import forms
from .models import Notes

class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ('title','body')
        widgets ={
            'title':forms.TextInput(attrs={'class':'form-control my-3'}),
            'body':forms.Textarea(attrs={'class':'form-control my-3'}),
        }
        labels = {
            "body" :'write your thoughts here'
        }
