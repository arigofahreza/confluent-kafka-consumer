from confluent_kafka import Consumer
from pydantic.v1 import BaseSettings


class KafkaConfig(BaseSettings):
    KAFKA_BOOTSTRAP: str
    KAFKA_GROUP_ID: str
    KAFKA_AUTO_OFFSET_RESET: str
    KAFKA_AUTO_COMMIT: str
    KAFKA_TOPIC: str

    class Config:
        env_file = ".env"


def consumer() -> Consumer:
    kafka_config = KafkaConfig()
    consumer_client = Consumer(
        {
            "bootstrap.servers": kafka_config.KAFKA_BOOTSTRAP,
            "group.id": kafka_config.KAFKA_GROUP_ID,
            "auto.offset.reset": kafka_config.KAFKA_AUTO_OFFSET_RESET
        }
    )
    consumer_client.subscribe([kafka_config.KAFKA_TOPIC])
    return consumer_client
