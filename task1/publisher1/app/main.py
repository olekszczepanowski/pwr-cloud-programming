import time
import sys
from ..domain.events.Type1Event import Type1Event
import pika
import logging


def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

    channel = connection.channel()

    queue_name = Type1Event.__name__
    channel.queue_declare(queue=queue_name)
    print(' [*] Waiting for messages. To exit press CTRL+C')
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    messageID = 1

    while True:
        event = Type1Event("event1", str({"message": f"Event1 - Message {messageID}"}))
        channel.basic_publish(exchange='', routing_key=queue_name, body=event.serialize())
        logging.info(f"Published event: {event}")
        messageID += 1
        time.sleep(2)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logging.info("Publisher 1 interupted.")
        sys.exit(0)
