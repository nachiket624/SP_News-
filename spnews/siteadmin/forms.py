from django import forms
from .models import News
from django.forms import ModelForm, TextInput, EmailInput, Textarea

class DraftNews(forms.ModelForm):
    class Meta:
        model = News
        widgets = {'status': forms.HiddenInput()}
        fields = ["headding", "para1", "para2", "img", "tag", "location"]
        labels = {"headding": "Hedding", "para1": "Pragraph 1", "para2": "Paragraph 2",
                  "img": "Upload Image", "tag": "Tag's", "location": "Loaction"}

        widgets = {
            'headding': Textarea(attrs={
                'class': "form-control border border-dark",
                'id': 'exampleFormControlTextarea1',
                'rows': '3',
            }),
            'para1': Textarea(attrs={
                'class': "form-control border border-dark",
                "id": "exampleFormControlTextarea1",
                "rows": "10"
            }),
            'para2': Textarea(attrs={
                'class': "form-control border border-dark",
                "id": "exampleFormControlTextarea1",
                "rows": "10"
            }),
            'tag': TextInput(attrs={
                "class": "form-control form-control-lg border border-dark",
                "type": "text",
                "aria-label": ".form-control-lg example"
            }),
            'location': TextInput(attrs={
                "class": "form-control form-control-lg border border-dark",
                "type": "text",
                "aria-label": ".form-control-lg example"
            }),
        }
