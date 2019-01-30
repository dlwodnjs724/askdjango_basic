from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

    '''
    def save(self, commit=True):
        post = Post.objects.create(**self.cleaned_data)
        if commit:
            post.save()
        return post
    '''
