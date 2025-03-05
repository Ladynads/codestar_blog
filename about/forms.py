from django import forms
from blog.models import CollaborateRequest  # Use absolute import

class CollaborateForm(forms.ModelForm):
    class Meta:
        model = CollaborateRequest
        fields = ['name', 'email', 'message']