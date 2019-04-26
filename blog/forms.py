from django import forms

from .models import Clanky, Comment

class ClankyForm(forms.ModelForm):

    class Meta:
        model = Clanky
        fields = ('title', 'text',)

# komentare
class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)
