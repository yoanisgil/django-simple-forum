from django import forms
from forum.models import Topic, Post

class TopicForm(forms.ModelForm):

    title = forms.CharField(max_length=60, required=True)

    class Meta():
        model = Topic
        exclude = ('creator','updated', 'created', 'closed', 'forum',)


class PostForm(forms.ModelForm):
    
    class Meta():
        model = Post
        exclude = ('creator', 'updated', 'created','topic', 'user_ip',)
