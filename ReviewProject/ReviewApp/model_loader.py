from transformers import BertTokenizer, BertForSequenceClassification
import os
import torch

def predict_review(text):

    model_path = os.path.join( "ReviewApp", "models")

    tokenizer = BertTokenizer.from_pretrained(model_path)
    model = BertForSequenceClassification.from_pretrained(model_path)

    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True, max_length=512)

    with torch.no_grad():
        outputs = model(**inputs)

    logits = outputs.logits
    predicted_class = torch.argmax(logits).item()

    sentiment = "Positive" if predicted_class == 1 else "Negative"

    return sentiment