from django.urls import path
from .views import classify_review_api,review_form

urlpatterns = [
    path("", review_form, name="home"), 
    path("classify/", classify_review_api, name="classify_review"),
]
