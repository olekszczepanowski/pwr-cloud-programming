import time
import sys
from ..domain.events.Type2Event import Type2Event
import pika
import logging


def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

    channel = connection.channel()

    queue_name = Type2Event.__name__
    channel.queue_declare(queue=queue_name)
    print(' [*] Waiting for messages. To exit press CTRL+C')
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    def callback(ch, method, properties, body):
        event = Type2Event.deserialize(body)
        logging.info(f"Received event: {event}")
        ch.basic_ack(delivery_tag=method.delivery_tag)
        time.sleep(3)

    channel.basic_consume(queue=queue_name, on_message_callback=callback)
    channel.start_consuming()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logging.info("Consumer 2 interupted.")
        sys.exit(0)
