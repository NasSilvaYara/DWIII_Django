from django import forms
from .models import Produto

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = '__all__'

    def clean_preco(self):
        preco = self.cleaned_data.get('preco')
        if preco is not None and preco <= 0:
            raise forms.ValidationError("O preço deve ser maior que zero.")
        return preco

    def clean_estoque(self):
        estoque = self.cleaned_data.get('estoque')
        if estoque is not None and estoque < 0:
            raise forms.ValidationError("A quantidade em estoque não pode ser negativa.")
        return estoque