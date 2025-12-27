from django import forms

from catalog.models import Contact, Product, Version


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'phone', 'message']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ('created', 'creator')

    bad_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']
        for bad_word in self.bad_words:
            if bad_word in cleaned_data.lower():
                raise forms.ValidationError('В наименовании товара не должно быть запрещенных слов')
        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data['description']
        for bad_word in self.bad_words:
            if bad_word in cleaned_data.lower():
                raise forms.ValidationError('В описании товара не должно быть запрещенных слов')
        return cleaned_data


class VersionForm(forms.ModelForm):
    class Meta:
        model = Version
        fields = ('name', 'number', 'flag')

    def clean_flag(self):
        cleaned_data = self.cleaned_data['flag']
        product_id = self.instance.product.pk
        current_version_id = self.instance.pk
        active_versions = Version.objects.filter(product=product_id, flag=True).exclude(id=current_version_id)
        if cleaned_data and active_versions.exists():
            raise forms.ValidationError('Должна быть только одна активная версия')
        return cleaned_data
