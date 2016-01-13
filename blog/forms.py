from django import forms

from models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text', 'parent']
        widgets = {
            'parent': forms.HiddenInput,
            # 'text': forms.Textarea(attrs={'autofocus': True})
        }
