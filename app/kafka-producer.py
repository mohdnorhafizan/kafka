from kafka import KafkaProducer
import json

producer = KafkaProducer(
    bootstrap_servers="localhost:29092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

with open("data/test.json", "r") as file:
    messages = json.load(file)

for message in messages:
    print("Sending message:", message)

    producer.send("operation-log", value=message)
    producer.flush()

    print("Message sent")