from django import forms
from rksite.models import Message

class EmailForm(forms.ModelForm):
    name = forms.CharField(max_length=200,help_text="Name:")
    email = forms.EmailField(help_text="Email:")
    subject = forms.CharField(max_length=100, help_text="Subject:")
    message = forms.CharField(max_length=1000, widget=forms.Textarea, help_text="Message:")

    class Meta:
        model = Message #link the model to the form
