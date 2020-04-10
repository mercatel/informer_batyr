from django import forms

from batyr.models import CommentCategory, Comment


class CommentForm(forms.ModelForm):
    category_comment = forms.ModelChoiceField(queryset=CommentCategory.objects.all(), label="ВСКРО")

    class Meta:
        model = Comment

        fields = ['category_comment', 'comment_txt', ]
        exclude = ['comment_create', 'comment_check', ]
