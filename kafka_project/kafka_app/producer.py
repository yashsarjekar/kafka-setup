from confluent_kafka import Producer
import json

conf = {'bootstrap.servers': 'b-2.kafka.xapgpx.c3.kafka.ap-south-1.amazonaws.com:9092,b-1.kafka.xapgpx.c3.kafka.ap-south-1.amazonaws.com:9092'}

producer = Producer(conf)

def delivery_report(err, msg):
    """ Delivery report handler called on
        successful or failed delivery of message """
    if err is not None:
        print(f'Message delivery failed: {err}')
    else:
        print(f'Message delivered to {msg.topic()} [{msg.partition()}]')

def send_message(json_data):
    try:
        producer.produce('test-topic', value=json.dumps(json_data), callback=delivery_report)
        producer.poll(1)
        print("Message sent successfully")
    except Exception as e:
        print(f"Failed to send message: {str(e)}")

# Example JSON message
json_data = {
    "id": 123,
    "name": "John Doe",
    "email": "johndoe@example.com",
    "message": "This is a JSON message"
}

send_message(json_data)
