from loguru import logger

from confluent_kafka_consumer.src.config.kafka import consumer
from confluent_kafka import KafkaError

app = typer.Typer()


@app.command()
def produce_message():
    ConsumerService().consume()


class ConsumerService:
    def __init__(self):
        self._consumer_client = consumer()

    def consume(self):
        try:
            while True:
                message = self._consumer_client.poll(1)
                if message is None:
                    continue
                logger.info(message)
                consumer().commit(message)
        except KeyboardInterrupt:
            pass
        finally:
            consumer().close()
