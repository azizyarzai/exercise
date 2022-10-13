from django import forms


class TestForm(forms.Form):
    name = forms.CharField(
        max_length=10)
    # name_hi = forms.CharField(
    #     max_length=10, label="Test", widget=forms.Textarea)
    age = forms.IntegerField()
    password = forms.PasswordInput()
