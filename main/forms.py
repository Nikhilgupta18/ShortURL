from django import forms
from .validators import validate_url
from .models import UrlShort


class SubmitURLForm(forms.Form):
    url = forms.CharField(
        label='',
        validators=[validate_url],
        widget=forms.TextInput(
            attrs={'placeholder': 'Your Links'}
        )
    )

    class Meta:
        model = UrlShort

        help_texts = {
            'url': 'Shorten your URL here'
        }

    # def __init__(self, title, desc, *args, **kwargs):
    #     self.title = title
    #     self.desc = desc
    #     super(SubmitURLForm, self).__init__(*args, **kwargs)

    # def clean(self):
    #     cleaned_data = super(SubmitURLForm, self).clean()
    #     url = cleaned_data.get('url')
    #     url_validators = URLValidator()
    #     try:
    #         url_validators(url)
    #     except:
    #         raise forms.ValidationError("Invalid URL")
    #
    #     return url
