from django import forms
from recipe_app.models import Author

class recipe_form(forms.Form):
    title = forms.CharField(max_length=50)
    time_required = forms.CharField(max_length=20)
    description = forms.CharField(widget=forms.Textarea)
    instructions = forms.CharField(widget=forms.Textarea)
    author = forms.ModelChoiceField(queryset=Author.objects.all())


class author_form(forms.Form):
    name = forms.CharField(max_length=50)
    bio = forms.CharField(widget=forms.Textarea)


"""class Author(models.Model):
    name = models.CharField(max_length=50)
    bio = models.TextField()
    def __str__(self):
        return self.name

class Recipe(models.Model):
    title = models.CharField(max_length=50)
    time_required = models.CharField(max_length=20)
    description = models.TextField()
    instructions = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    def __str__(self):
        return self.title
        """