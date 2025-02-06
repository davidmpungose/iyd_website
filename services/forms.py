from django import forms
from .models import BlogPost, BlogCategory
from ckeditor.fields import RichTextField

class PostForm(forms.ModelForm):
    content = RichTextField()

    class Meta:
        model = BlogPost
        fields = ('title', 'category','image', 'author', 'content', 'title_tag')

    def clean(self):
        cleaned_data = super(PostForm, self).clean()
        category = cleaned_data.get('category')
        category_name = cleaned_data.get('category_name')

        if not category and not category_name:
            raise forms.ValidationError('Please select a category or enter a new category name.')

        # Handle logic for creating a new category if category_name is provided
        if category_name:
            new_category = BlogCategory.objects.create(name=category_name)
            cleaned_data['category'] = new_category  # Update category in cleaned data

        return cleaned_data
    
class CategoryForm(forms.ModelForm):
    class Meta:
        model = BlogCategory
        fields = ['name']
