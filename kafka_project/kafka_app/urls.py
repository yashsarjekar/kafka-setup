from django.urls import path
from .views import produce_kafka_message

urlpatterns = [
    path('send-message/', produce_kafka_message),
]
