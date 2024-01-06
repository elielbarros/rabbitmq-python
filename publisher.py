import pika
import json


class RabbitmqPublisher:
    def __init__(self):
        self.__host = 'localhost'
        self.__port = 5672
        self.__username = 'guest'
        self.__password = 'guest'
        self.__exchange = 'python-exchange'
        self.__routing_key = ''
        self.__channel = self.create_channel()

    def create_channel(self):
        connection_parameters = pika.ConnectionParameters(
                host=self.__host,
                port=self.__port,
                credentials=pika.PlainCredentials(
                        username=self.__username,
                        password=self.__password
                )
        )

        return pika.BlockingConnection(connection_parameters).channel()

    def send_message(self, body):
        self.__channel.basic_publish(
                exchange=self.__exchange,
                routing_key=self.__routing_key,
                body=json.dumps(body),
                properties=pika.BasicProperties(
                        delivery_mode=2
                )
        )


publisher = RabbitmqPublisher()
publisher.send_message({'key': 'value'})
