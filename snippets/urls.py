from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

urlpatterns = [
    path('snippets_list/<int:pk>/', views.SnippetList.as_view()),
    path('snippets_details/<int:pk>', views.SnippetDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)