from django.urls import path
from .views import ResourceView, ResourceDetailView

urlpatterns = [
    path('', ResourceView.as_view()),
    path('<int:id>/', ResourceDetailView.as_view())
]