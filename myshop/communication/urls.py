from django.urls import path

from communication.views import FeedbackView, info_view


urlpatterns = [
    path('feedback/', FeedbackView.as_view(), name='feedback'),
    path('info/', info_view, name='info'),
]
