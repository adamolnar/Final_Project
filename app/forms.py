from django import forms
from .models import Post, Comment, Contact, Tag



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',) 

class CustomMMCF(forms.ModelMultipleChoiceField):
    def label_from_instance(self, tags):
        return "%s" % tags.name    


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','content','featured_image', 'status', 'categories', 'tags')

        title = forms.CharField()
        content = forms.CharField()
        featured_image = forms.ImageField()
        status = forms.IntegerField()

        categories = forms.ModelMultipleChoiceField(
          queryset=Tag.objects.all(),
          widget=forms.CheckboxSelectMultiple
        )
        # Update the form to allow users to select multiple tags.
        tags = CustomMMCF(
          queryset=Tag.objects.all(),
          widget=forms.CheckboxSelectMultiple
        )


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

# create a search form to filter the explore page by other tags, 
# allowing the user to search for posts with specific tags    
# class ExploreForm(forms.Form):
#   query = forms.CharField(
#   label='',
#   widget=forms.TextInput(attrs={
#     'placeholder': 'Explore tags'
#     })
#   )
    