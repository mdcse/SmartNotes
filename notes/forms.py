from django import forms
from.models import Notes

class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ('title', 'content')
        labels = {'content': "note content", 'title': "note title"}
        widgets = {
            'title': forms.TextInput(attrs={'class': "form-control my-5"}),
            'content': forms.Textarea(attrs={'class': "form-control mb-5"}),
        
        }
        
        

    def clean_title(self):
        title = self.cleaned_data['title']
        if "Django" not in title:            
            raise forms.ValidationError("You need to write about Dango")
        else:
            return title