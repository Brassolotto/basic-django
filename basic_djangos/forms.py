from djando import forms
from .models import Topic

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}
# The TopicForm class inherits from forms.ModelForm, a parent class included in Django that helps build forms from models. The Meta class tells Django which model to base the form on and which fields to include in the form. The labels attribute provides a label for each field in the form. In this case, we're telling Django not to generate a label for the text field.

    