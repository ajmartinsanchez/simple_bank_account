import re
from home.models import ClientBank
from django import forms

REGULAR_EXPRESION = "[a-zA-Z]{2}[0-9]{2}[a-zA-Z0-9]{4}[0-9]{7}([a-zA-Z0-9]?){0,16}"

class ClientForm(forms.ModelForm):
    class Meta:
        model = ClientBank
        fields = ('firstname', 'lastname', 'iban')

    def clean(self):
        cleaned_data = super(ClientForm, self).clean()
        iban = cleaned_data.get('iban')
        pattern = re.compile(REGULAR_EXPRESION)
        if not pattern.match(iban):
            raise forms.ValidationError("Iban format error")

        return super(ClientForm, self).clean()

    def save(self, creator=None, commit=False):
        instance = super(ClientForm, self).save(commit=False)

        if creator:
            instance.creator = creator

        instance.save()


