# author wangz
from django import forms


class CommentsForm(forms.Form):
    comment = forms.CharField(required=True)