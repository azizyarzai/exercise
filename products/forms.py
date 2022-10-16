from django import forms

from products.models import Product


class TestForm(forms.Form):
    name = forms.CharField(
        max_length=10, error_messages={'required': 'Please enter your name'})
    # name_hi = forms.CharField(
    #     max_length=10, label="Test", widget=forms.Textarea)
    age = forms.IntegerField()
    password = forms.PasswordInput()
    time = forms.DurationField()
    # email = forms.EmailField()
    image = forms.FileField(error_messages={'empty': 'Your file is empty.'})


class ProductModelForm(forms.ModelForm):
    class Meta:
        model = Product
        # fields = ['name', 'price']
        fields = '__all__'
        exclude = ['slug']
