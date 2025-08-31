#  Real-Time Log Analytics Pipeline (Fully Automated)

This project implements a **real-time log analytics pipeline** where:
- **Kafka** streams logs
- **Spark Structured Streaming** processes logs
- **Elasticsearch** stores logs
- **Kibana** visualizes logs

##  How It Works Automatically
1. Run:
   ```bash
   docker-compose up -d --build
   ```

2. What happens:
   - Zookeeper + Kafka start
   - `kafka-init` creates topic `logs`
   - `producer` sends logs into Kafka
   - `spark` consumes logs and writes to Elasticsearch
   - `elasticsearch` stores logs in index `logs-index`
   - `kibana` UI available at http://localhost:5601

3. Open Kibana:
   - Go to http://localhost:5601
   - Create index pattern: `logs-index*`
   - Build dashboards (ERROR vs INFO, trends, etc.)

  Use Cases
- Monitor application logs
- Detect errors in real-time
- Security event tracking
