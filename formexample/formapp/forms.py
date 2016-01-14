from django import forms


class HelloWorldForm(forms.Form):
    name = forms.CharField(label="Say Hello")
    awesome = forms.BooleanField(label="Are they awesome?", required=False)

    def clean_name(self):
        name = self.cleaned_data['name']
        if not name.lower().startswith('b'):
            raise forms.ValidationError("Wait a second, %s doesn't start with B!" % name)
        return name
