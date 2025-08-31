from kafka import KafkaProducer
import json, time, random

producer = KafkaProducer(
    bootstrap_servers='kafka:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

logs = [
    "INFO: User logged in",
    "ERROR: Database connection failed",
    "WARNING: High memory usage",
    "INFO: API request successful",
    "ERROR: Unauthorized access attempt"
]

while True:
    log = {"event": random.choice(logs)}
    producer.send("logs", log)
    print(f"Sent: {log}")
    time.sleep(2)
