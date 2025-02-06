from django.urls import path
from . import views

urlpatterns = [
    path('blog/', views.BlogView.as_view(), name='blog-home'),
    path('article/<int:pk>', views.ArticleDetailView.as_view(), name='article-detail'),
    path('article/<int:pk>/edit', views.UpdatePostView.as_view(), name='edit-article'),
    path('add-article/', views.create_post, name= 'add-article'),
    path('add-category/', views.create_category, name= 'add-category'),
    
]