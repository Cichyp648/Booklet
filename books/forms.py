from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'genre', 'year']
        widgets = {
           'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
           'director': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Author', 'rows': 1}),
           'release_year': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Year of publication'}),
           'genre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Genre'}),
}

# Add ReviewForm (if you're using it now)
class ReviewForm(forms.Form):
    rating = forms.IntegerField(
        min_value=1,
        max_value=5,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Rating 1–5'})
    )
