from django import forms
from .submodels import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)

    comment = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Yorum yaz..', 'class': 'form__textarea'}))