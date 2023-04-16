from django.urls import path

from communication.views import FeedbackView

urlpatterns = [
    path('feedback/', FeedbackView.as_view(), name='feedback'),
]
