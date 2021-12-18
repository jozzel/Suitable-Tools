from django import forms
from django.core import validators
from django.core.validators import validate_unicode_slug
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User as auth_user

from . import models


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(
        label="Email",
        required=True,
        #validators=[must_be_unique]
    )
    
    class Meta:
        model = auth_user
        fields = (
            "username",
            "email",
            "password1",
            "password2"
        )
    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class CommentForm(forms.Form):
    comment_field = forms.CharField(
        label='Comment',
        max_length=240,
        # validators=[validate_unicode_slug, must_be_caps, must_be_bob]
        )

    def save(self, request):
        comment_instance = models.CommentModel()
        comment_instance.comment = self.cleaned_data["comment_field"]
        comment_instance.author = request.user
        comment_instance.save()
        return comment_instance