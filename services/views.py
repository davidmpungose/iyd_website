from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib import messages
from .models import BlogPost, BlogCategory
from .forms import PostForm, CategoryForm

# def BlogView(request):
#     return render(request, 'blog/uc.html')


class BlogView(ListView):
    model = BlogPost
    template_name = 'blog/blog_plus.html'
    paginate_by = 5

    def get_queryset(self):
        return super().get_queryset().order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super(BlogView, self).get_context_data(**kwargs)
        categories = BlogCategory.objects.all()
        context['categories'] = categories
        return context

class PostView(ListView):
    model = BlogPost
    template_name = 'blog/post.html'

class ArticleDetailView(DetailView):
    model = BlogPost
    template_name = 'blog/article_details.html'

    def get_context_data(self, **kwargs: Any): 
        context = super().get_context_data(**kwargs)
        context['post'] = self.object
        return context

class AddPostView(CreateView):
    model = BlogPost
    template_name = 'blog/add_article.html'
    fields = '__all__'


class UpdatePostView(UpdateView):
    model = BlogPost
    template_name = 'blog/edit_post.html'
    fields = ['title', 'title_tag', 'image', 'content']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = self.object  # Pass the current blog post object
        return context

def some_view(request):
    categories = BlogCategory.objects.all()
    context = {'categories': categories}
    return render(request, 'blog_plus.html', context)

@login_required
def create_post(request):
    post_form = PostForm()
    category_form = CategoryForm()

    if request.method == 'POST':
        if 'post_submit' in request.POST:  # Check if the post submit button was clicked
            post_form = PostForm(request.POST, request.FILES)
            if post_form.is_valid():
                new_post = post_form.save(commit=False)
                new_post.author = request.user

                # Handle category selection (existing or new)
                category_id = request.POST.get('category')
                if category_id:
                    new_post.category = BlogCategory.objects.get(pk=category_id)
                else:  # No category selected, try creating a new one
                    category_name = request.POST.get('new_category')
                    if category_name:
                        new_category = BlogCategory.objects.create(name=category_name)
                        new_post.category = new_category  # Assign the newly created category
                    else:
                        # Handle the case where no category is selected and no new category name is provided
                        # You might want to set a default category or display an error message
                        messages.error(request, "Please select a category or enter a new category name.")
                        return render(request, 'blog/add_article.html', {'form': post_form, 'category_form': category_form})

                new_post.save()
                messages.info(request, 'New Blog Post Added Successfully.')
                return redirect('blog-home')
            else:
                messages.warning(request, 'Something went wrong with the post.')
                # Re-render the form with errors

        elif 'category_submit' in request.POST:  # Check if category form was submitted
            category_form = CategoryForm(request.POST)
            if category_form.is_valid():
                category_form.save()
                messages.info(request, 'New Category Added Successfully.')
                return redirect('create-post')  # Redirect back to the create post page
            else:
                messages.warning(request, 'Something went wrong with the category.')
                # Re-render the category form with errors

    context = {'form': post_form, 'category_form': category_form}
    return render(request, 'blog/add_article.html', context)

@login_required
def create_category(request): # independent view for adding a category
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category created successfully!')
            return redirect('blog-home')  # Redirect to wherever appropriate
        else:
            messages.error(request, 'Error creating category.')
    else:
        form = CategoryForm()
    return render(request, 'blog/add_category.html', {'form': form})

@login_required
def create_category(request):  # Independent view for adding a category
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()  # Now this will save the category
            messages.success(request, 'Category created successfully!')
            return redirect('create-post')  # Redirect back to the create post page so you can see it in dropdown
        else:
            messages.error(request, 'Error creating category.')
    else:
        form = CategoryForm()
    return render(request, 'blog/add_category.html', {'form': form})