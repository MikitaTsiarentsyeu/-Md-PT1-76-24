from typing import Any
from django import forms
from .models import Post
from django.core.exceptions import ValidationError

class AddPostForm(forms.Form):

    title = forms.CharField(max_length=Post.TITLE_MAX_LENGTH, label="Title")
    content = forms.CharField(widget=forms.Textarea(), label="Content")
    post_type = forms.ChoiceField(choices=Post.POST_TYPES, label="Post type")
    image = forms.ImageField(label="Main image")

    def clean_title(self):
        title_data = self.cleaned_data['title']
        title_data = format_text_value(title_data)

        if title_data == "test":
            raise ValidationError("Please enter not a test value")

        return title_data


    def clean_content(self):
        content_data = self.cleaned_data['content']
        content_data = format_text_value(content_data)

        if content_data == "test":
            raise ValidationError("Please enter not a test value")
        
        try:
            title_data = self.cleaned_data['title']
        except KeyError:
            raise ValidationError("Please fill title with a correct value")
        
        if content_data == title_data:
            raise ValidationError("Content cannot has the same value as title")

        return content_data
        

def format_text_value(value):
    return value.strip().lower()


class AddPostModelForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'content', 'post_type', 'image')