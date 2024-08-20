from django.urls import path
from .views import AddToQueueView, CurrentMatchView, ProcessMatchingView

urlpatterns = [
    path('add-to-queue/', AddToQueueView.as_view(), name='add-to-queue'),
    path('process-matching/', ProcessMatchingView.as_view(), name='process-matching'),
    path('current-match/', CurrentMatchView.as_view(), name='current-match'),
]