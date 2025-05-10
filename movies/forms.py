from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'director', 'release_year', 'genre']
        widgets = {
    'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
    'director': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Director', 'rows': 1}),
    'release_year': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Year of release'}),
    'genre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Movie genre'}),
}

