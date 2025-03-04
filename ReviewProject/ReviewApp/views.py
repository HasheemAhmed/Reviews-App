from rest_framework.response import Response
from rest_framework.decorators import api_view
from .model_loader import predict_review

@api_view(["POST"])
def classify_review_api(request):
    review_text = request.data.get("review", "")

    if not review_text:
        return Response({"error": "No review text provided"}, status=400)

    sentiment = predict_review(review_text)
    return Response({"review": review_text, "sentiment": sentiment})

from django.shortcuts import render

def review_form(request):
    return render(request, "index.html")

