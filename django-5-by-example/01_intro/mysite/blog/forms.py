from django import forms
from .models import Comment


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)


class CommentForm(forms.ModelForm):
    # To create a form from a model, we just indicate which model to build the form for in the Meta
    # class of the form. Django will introspect the model and build the corresponding form dynamically.
    class Meta:
        model = Comment
        fields = ["name", "email", "body"]
