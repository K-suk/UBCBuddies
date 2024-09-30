from django.urls import path
from .views import AddToQueueView, CurrentMatchView, ProcessMatchingView, SubmitReviewView

urlpatterns = [
    path('add-to-queue/', AddToQueueView.as_view(), name='add-to-queue'),
    path('process-matching/', ProcessMatchingView.as_view(), name='process-matching'),
    path('current-match/', CurrentMatchView.as_view(), name='current-match'),
    path('submit-review/', SubmitReviewView.as_view(), name='submit-review'),
]