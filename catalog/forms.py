from django import forms

from catalog.models import Contact, Product


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'phone', 'message']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ('created', )
