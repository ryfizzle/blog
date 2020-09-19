from django.urls import path
from . import views
urlpatterns = [
    path('',views.PostList.as_view(),name = 'list'),
    path('<int:pk>/post',views.PostDetail.as_view(),name = 'detail'),
    path('create',views.CreatePost.as_view(),name = 'create'),
    path('<int:pk>/delete',views.PostDelete.as_view(),name = 'delete'),
    path('<int:pk>/update',views.PostUpdate.as_view(),name = 'update'),
    
]
