from django.urls import path
from .views import (
    PostListView,
    PostCreateView,
    PostDetailView,
    PostUpdateView,
    PostDeleteView,
    TypePostListView,
    SearchResultView,
    )
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('new/', PostCreateView.as_view(), name='add'),
    path('<int:pk>/', PostDetailView.as_view(), name='detail'),
    path('<int:pk>/update', PostUpdateView.as_view(), name='update'),
    path('<int:pk>/delete', PostDeleteView.as_view(), name='delete'),
    path('type/<str:pk>', TypePostListView.as_view(), name='type'),
    path('search/', SearchResultView.as_view(), name='search'),
]
