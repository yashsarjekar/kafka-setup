const { Kafka } = require('kafkajs');

const kafka = new Kafka({
  clientId: 'my-consumer',
  brokers: [
	'b-2.kafka.xapgpx.c3.kafka.ap-south-1.amazonaws.com:9092',
	'b-1.kafka.xapgpx.c3.kafka.ap-south-1.amazonaws.com:9092'
]
});

const consumer = kafka.consumer({ groupId: 'test-group' });

const run = async () => {
  await consumer.connect();
  await consumer.subscribe({ topic: 'test-topic', fromBeginning: true });

  await consumer.run({
    eachMessage: async ({ topic, partition, message }) => {
      const receivedData = JSON.parse(message.value.toString());
      console.log(`Received message:`, receivedData);
      console.log(`Name field:`,receivedData.name)
    },
  });
};

run().catch(console.error);
