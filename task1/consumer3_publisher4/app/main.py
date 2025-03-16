import time
import sys
from ..domain.events.Type3Event import Type3Event
from ..domain.events.Type4Event import Type4Event
import pika
import logging


def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

    channel = connection.channel()

    consumer_queue_name = Type3Event.__name__
    channel.queue_declare(queue=consumer_queue_name)

    publisher_queue_name = Type4Event.__name__
    channel.queue_declare(queue=publisher_queue_name)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    temporary = 1

    def callback(ch, method, properties, body):
        nonlocal temporary
        event = Type3Event.deserialize(body)
        logging.info(f"Received event: {event}")
        ch.basic_ack(delivery_tag=method.delivery_tag)
        time.sleep(2)
        new_event = Type4Event("event4", str({"message": f"Event4 - Message {temporary}"}))
        channel.basic_publish(exchange='', routing_key=publisher_queue_name, body=new_event.serialize())
        logging.info(f"Published event: {new_event}")
        temporary += 1

    channel.basic_consume(queue=consumer_queue_name, on_message_callback=callback)
    channel.start_consuming()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logging.info("Consumer 3 Publisher 4 interupted.")
        sys.exit(0)
