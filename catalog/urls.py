from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('articles/', views.ArticleListView.as_view(), name='articles'),
  path('articles/<int:pk>', views.ArticleDetailView.as_view(), name='article-detail'),
  path('students/<int:pk>', views.StudentDetailView.as_view(), name='student-detail'),
  path('mytests/', views.DueTestsByUserListView.as_view(), name='my-tests'),
  #path('article/<id:pk>/test/', views.test_article_teacher, name='test-article-teacher'),
]

urlpatterns += [
    path('student/create/', views.StudentCreate.as_view(), name='student-create'),
    path('student/<int:pk>/update/', views.StudentUpdate.as_view(), name='student-update'),
    path('student/<int:pk>/delete/', views.StudentDelete.as_view(), name='student-delete'),
]



