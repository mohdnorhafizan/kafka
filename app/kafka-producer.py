from kafka import KafkaProducer
import json

producer = KafkaProducer(
    bootstrap_servers="localhost:29092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

message = {
    "id": 2,
    "name": "Hafizan",
    "message": "Nice its working!"
}

producer.send("operation-log", value=message)
producer.flush()

print("Message sent")