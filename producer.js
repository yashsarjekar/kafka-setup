const { Kafka } = require('kafkajs');

const kafka = new Kafka({
  clientId: 'my-producer',
  brokers: [
	'b-2.kafka.xapgpx.c3.kafka.ap-south-1.amazonaws.com:9092',
	'b-1.kafka.xapgpx.c3.kafka.ap-south-1.amazonaws.com:9092'
	]
});

const producer = kafka.producer();

const jsonData = {
  id: 123,
  name: "John Doe",
  email: "johndoe@example.com",
  message: "This is a JSON message"
};

const run = async () => {
  await producer.connect();
  await producer.send({
    topic: 'test-topic',
    messages: [
      { value: JSON.stringify(jsonData) },
    ],
  });
  console.log("Message sent successfully");
  await producer.disconnect();
};

run().catch(console.error);
