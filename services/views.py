from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib import messages
from .models import BlogPost, BlogCategory
from .forms import PostForm

def BlogView(request):
    return render(request, 'blog/uc.html')


# class BlogView(ListView):
#     model = BlogPost
#     template_name = 'blog/blog_plus.html'
#     paginate_by = 5

#     def get_queryset(self):
#         return super().get_queryset().order_by('-created_at')

#     def get_context_data(self, **kwargs):
#         context = super(BlogView, self).get_context_data(**kwargs)
#         categories = BlogCategory.objects.all()
#         context['categories'] = categories
#         return context

# class PostView(ListView):
#     model = BlogPost
#     template_name = 'blog/post.html'

# class ArticleDetailView(DetailView):
#     model = BlogPost
#     template_name = 'blog/article_details.html'

#     def get_context_data(self, **kwargs: Any): 
#         context = super().get_context_data(**kwargs)
#         context['post'] = self.object
#         return context

# class AddPostView(CreateView):
#     model = BlogPost
#     template_name = 'blog/add_article.html'
#     fields = '__all__'


# class UpdatePostView(UpdateView):
#     model = BlogPost
#     template_name = 'blog/edit_post.html'
#     fields = ['title', 'title_tag', 'image', 'content']

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['post'] = self.object  # Pass the current blog post object
#         return context

# def some_view(request):
#     categories = BlogCategory.objects.all()
#     context = {'categories': categories}
#     return render(request, 'blog_plus.html', context)

# @login_required  # Ensures only logged-in users can create posts
# def create_post(request):
#     if request.method == 'POST':
#         form = PostForm(request.POST, request.FILES)  # Include uploaded files
#         if form.is_valid():
#             # Create a new BlogPost object
#             new_post = form.save(commit=False)  # Don't save yet
#             new_post.author = request.user  # Set the current user as author

#             # Check if a category is selected (optional)
#             if 'category' in request.POST:
#                 selected_category = request.POST['category']
#                 new_post.category = BlogCategory.objects.get(pk=selected_category)

#             new_post.save()  # Now save the post to the database
#             messages.info(request, 'New Blog Post Added Successfully.')

#             return redirect('blog-home')  # Redirect to blog homepage after success
#         else:
#             messages.warning(request, 'Something went wrong.')
#             return redirect('blog-home')
#     else:
#         form = PostForm()

#     context = {'form': form}
#     return render(request, 'blog/add_article.html', context)