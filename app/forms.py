from django import forms
from app.models import *

class TopicModelForm(forms.ModelForm):
    class Meta():
        model = Topic
        fields = '__all__'

class WebpageModelForm(forms.ModelForm):
    class Meta():
        model = Webpage
        
        # Specific fields Displaying
        #fields = ['topicname','name','url']

        #exclude = ['name','url'] -- it excludes the specified columns and display remaining fields
        
        #Changing column Name Permanantly
        #labels = {'topicname':'topicss','name':'names'}

        # For applying properties on input box using widgets
        # A widget is Django's representation of an HTML input element. The widget handles the rendering of the HTML, and the extraction of data from a GET/POST dictionary that corresponds to the widget.
        #widgets = {'email':forms.PasswordInput}

        fields = '__all__'
        
class AccessModelForm(forms.ModelForm):
    class Meta():
        model = AccessRecord
        fields = '__all__'