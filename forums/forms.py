from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description', 'category']
        widgets = {'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
                   'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 8}),
                   'category': forms.Select(attrs={'class': 'form-control'}),
                   }
