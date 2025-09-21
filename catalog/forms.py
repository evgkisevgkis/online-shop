from django import forms

from catalog.models import Contact, Product, Version


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'phone', 'message']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ('created', )

    bad_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']
        for bad_word in self.bad_words:
            if bad_word in cleaned_data:
                raise forms.ValidationError('В наименовании товара не должно быть запрещенных слов')
        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data['description']
        for bad_word in self.bad_words:
            if bad_word in cleaned_data:
                raise forms.ValidationError('В описании товара не должно быть запрещенных слов')
        return cleaned_data


class VersionForm(forms.ModelForm):
    class Meta:
        model = Version
        fields = ('name', 'number', 'flag')

