from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = format_suffix_patterns([
    path('', views.api_root),
    path('snippets/', views.SnippetList.as_view(), name='snippet-list'),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view(), name='snippet-detail'),
    path('snippets/<int:pk>/highlight/', views.SnippetHighlight.as_view(), name='snippet-highlight'),
    path('provinces/', views.ProvinceList.as_view(), name='province-list'),
    path('province/<int:pk>/', views.ProvinceDetail.as_view(), name='province-detail'),
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail')
])




# urlpatterns = [
#     path('', views.api_root),
#     path('snippets/<int:pk>/highlight/', views.SnippetHighlight.as_view(), name='snippet-list'),
#     path('snippets/', views.SnippetList.as_view()),
#     path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
#     path('users/', views.UserList.as_view()),
#     path('users/<int:pk>/', views.UserDetail.as_view()),
# ]
#
# urlpatterns = format_suffix_patterns(urlpatterns)




# from django.urls import path
# from rest_framework.urlpatterns import format_suffix_patterns
# from . import views
#
# urlpatterns = [
#     path('snippets/', views.snippet_list),
#     path('snippets/<int:pk>/', views.snippet_detail),
# ]
#
# urlpatterns = format_suffix_patterns(urlpatterns)