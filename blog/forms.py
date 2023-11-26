from django import forms
from .models import Post
from django.core.validators import RegexValidator
from django.forms import ModelForm, inlineformset_factory, formset_factory

class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'category')  # Add 'category' to the list of fields
        widgets = {
            'title': forms.Textarea(attrs={'placeholder': 'Enter your title', 'style': 'font-size: 16px; font-weight: 500; width: 50%; height: 50px;'}),
            'content': forms.Textarea(attrs={'placeholder': 'Enter your content', 'style': 'font-size: 16px; font-weight: 500; width: 50%; height: 50px;'}),
            'category': forms.Select(attrs={'style': 'font-size: 16px; font-weight: 500; width: 50%; height: 50px;'}),
        }

Postformset = formset_factory(form=PostModelForm, extra=1)