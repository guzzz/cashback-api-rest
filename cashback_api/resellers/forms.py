from django import forms
from localflavor.br.forms import BRCPFField
from cashback_api.resellers.models import Reseller


class ResellerForm(forms.ModelForm):
    cpf = BRCPFField(label='CPF', required=True)

    class Meta:
        model = Reseller
        exclude = ('',)
