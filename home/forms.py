from django import forms
from .models.user_post import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content')
        widgets = {
            'title': forms.Textarea(attrs={'class': 'form-control custom-textarea', 'rows': 1,
                                             'placeholder': 'Add a title...'}),
            'content': forms.Textarea(attrs={'class': 'form-control custom-textarea', 'rows': 7,
                                             'placeholder': 'Add a post...'}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {
            'content': '',  # Set label to empty string
        }
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control custom-textarea', 'rows': 2,
                                             'placeholder': 'Add a comment...'}),
        }
