from django.urls import path
from . import views
urlpatterns = [
    path("messages/",views.MessagesView.as_view()),
]