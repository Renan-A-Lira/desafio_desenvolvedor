from django.forms import fields, widgets
from blog.models import Comment, Image
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Create your forms here.

class ImageForm(forms.ModelForm):
    	
	class Meta:
		model = Image
		fields = ['legenda', 'image_file']
		widgets = {
            'legenda': forms.TextInput(attrs={'class': 'legenda-form'}),
            'image_file': forms.FileInput(attrs={'class': 'text-form'})
        }

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ['text',]
		widgets = {
			'text': forms.Textarea(attrs={'class': 'comment-area', 'placeholder': 'comenente aqui...'})
		}


class UserForm(UserCreationForm):

	class Meta:
		model = User
		fields = ["username", "email", "password1", "password2"]

	def save(self, commit=True):
		user = super(UserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user