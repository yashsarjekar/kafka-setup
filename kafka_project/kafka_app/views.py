from django.shortcuts import render
from django.views.decorators.http import require_POST
# Create your views here.
from django.http import JsonResponse
from .producer import send_message
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
@require_POST
def produce_kafka_message(request):
    # Sample JSON data
    json_data = {
        "id": 123,
        "name": "Jane Doe",
        "email": "janedoe@example.com",
        "message": "Hello from Django"
    }
    
    send_message(json_data)
    return JsonResponse({"status": "Message sent successfully"})
