from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StringType

spark = SparkSession.builder     .appName("LogAnalyticsPipeline")     .config("spark.jars.packages", 
            "org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.0,"
            "org.elasticsearch:elasticsearch-spark-30_2.12:8.12.1")     .getOrCreate()

schema = StructType().add("event", StringType())

df = spark.readStream.format("kafka")     .option("kafka.bootstrap.servers", "kafka:9092")     .option("subscribe", "logs")     .load()

logs_df = df.selectExpr("CAST(value AS STRING)")     .select(from_json(col("value"), schema).alias("data"))     .select("data.event")

query_console = logs_df.writeStream     .outputMode("append")     .format("console")     .start()

query_es = logs_df.writeStream     .outputMode("append")     .format("org.elasticsearch.spark.sql")     .option("checkpointLocation", "/tmp/checkpoints/")     .option("es.nodes", "elasticsearch")     .option("es.port", "9200")     .start("logs-index")

query_console.awaitTermination()
query_es.awaitTermination()
