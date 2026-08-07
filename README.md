# Kafka Local Playground

A small local project for testing Kafka producer/consumer flows with Docker Compose.

It includes:
- Apache Kafka (single-node KRaft mode)
- Kafka UI (web dashboard)
- PostgreSQL
- Python producer and consumer scripts

## Project Structure

- `docker-compose.yml` - Infrastructure services (Kafka, Kafka UI, PostgreSQL)
- `app/kafka-producer.py` - Sends one JSON message to Kafka topic `operation-log`
- `app/kafka-consumer.py` - Consumes and prints messages from topic `operation-log`
- `kafka_data/` - Kafka persisted data directory
- `postgres_data/` - PostgreSQL persisted data directory

## Prerequisites

- Docker Desktop
- Python 3.9+
- pip

## Services and Ports

- Kafka external listener (host): `localhost:29092`
- Kafka internal listener (for containers): `kafka:9092`
- Kafka UI: `http://localhost:18080`
- PostgreSQL: `localhost:5432`

PostgreSQL defaults from compose:
- DB: `ai_db`
- User: `postgres`
- Password: `password123#`

## Quick Start

1. Start services:

```powershell
docker compose up -d
```

2. Install Python dependency:

```powershell
pip install kafka-python
```

3. Run consumer (terminal 1):

```powershell
python app/kafka-consumer.py
```

4. Run producer (terminal 2):

```powershell
python app/kafka-producer.py
```

Expected producer output:

```text
Message sent
```

Consumer should print the JSON payload from Kafka.

## Useful Kafka Commands

List topics:

```powershell
docker exec -it ai-platform-kafka-1 /opt/kafka/bin/kafka-topics.sh --bootstrap-server localhost:9092 --list
```

Describe topic:

```powershell
docker exec -it ai-platform-kafka-1 /opt/kafka/bin/kafka-topics.sh --bootstrap-server localhost:9092 --describe --topic operation-log
```

Create topic (if needed):

```powershell
docker exec -it ai-platform-kafka-1 /opt/kafka/bin/kafka-topics.sh --bootstrap-server localhost:9092 --create --topic operation-log --partitions 3 --replication-factor 1
```

Delete topic:

```powershell
docker exec -it ai-platform-kafka-1 /opt/kafka/bin/kafka-topics.sh --bootstrap-server localhost:9092 --delete --topic operation-log
```

## Kafka UI

Open:
- `http://localhost:18080`

Use Kafka UI to:
- Browse topics
- Inspect partitions and offsets
- View messages

## Reset Local Data (Optional)

If you want a clean local environment:

```powershell
docker compose down
```

Then remove persisted volumes:

```powershell
Remove-Item -Recurse -Force .\kafka_data
Remove-Item -Recurse -Force .\postgres_data
```

Recreate folders by bringing services back up:

```powershell
docker compose up -d
```

## Kafka Commands
### Delete Topic Message
```
docker exec -it ai-platform-kafka-1 /opt/kafka/bin/kafka-topics.sh --bootstrap-server localhost:9092 --delete --topic operation-log
```

## Notes

- The producer sends to topic `operation-log` on `localhost:29092`.
- The consumer reads from `earliest`, so it can replay existing records in the topic.
- Because data is persisted to local folders, messages and DB data survive container restarts unless directories are deleted.
