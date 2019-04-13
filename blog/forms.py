from django import forms

from .models import Clanky

class ClankyForm(forms.ModelForm):

    class Meta:
        model = Clanky
        fields = ('title', 'text',)
