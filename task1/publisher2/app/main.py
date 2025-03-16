import time
import sys
from ..domain.events.Type2Event import Type2Event
import pika
import logging
import random

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

    channel = connection.channel()

    queue_name = Type2Event.__name__
    channel.queue_declare(queue=queue_name)
    print(' [*] Waiting for messages. To exit press CTRL+C')
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    temporary = 1

    while True:
        event = Type2Event("event2", str({"message": f"Event2 - Message {temporary}"}))
        channel.basic_publish(exchange='', routing_key=queue_name, body=event.to_json())
        logging.info(f"Published event: {event}")
        temporary += 1
        time.sleep(random.randint(1, 6))


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logging.info("Publisher 2 interupted.")
        sys.exit(0)
