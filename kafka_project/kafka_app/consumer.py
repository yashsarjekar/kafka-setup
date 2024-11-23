from confluent_kafka import Consumer, KafkaException
import json

conf = {
    'bootstrap.servers': 'b-2.kafka.xapgpx.c3.kafka.ap-south-1.amazonaws.com:9092,b-1.kafka.xapgpx.c3.kafka.ap-south-1.amazonaws.com:9092',
    'group.id': 'test-group',
    'auto.offset.reset': 'earliest'
}

consumer = Consumer(conf)
consumer.subscribe(['test-topic'])

def consume_messages():
    try:
        while True:
            msg = consumer.poll(1.0)
            if msg is None:
                continue
            if msg.error():
                raise KafkaException(msg.error())
            else:
                json_data = json.loads(msg.value().decode('utf-8'))
                print(f"Received message: {json_data}")
                print(f"Name: {json_data['name']}")
    except Exception as e:
        print(f"Error while consuming: {str(e)}")
    finally:
        consumer.close()

consume_messages()
