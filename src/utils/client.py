import ssl
import pika
import os


class Client:

    def __init__(self, rabbitmq_broker_id, rabbitmq_user, rabbitmq_password, region):

        # SSL Context for TLS configuration of Amazon MQ for RabbitMQ
        ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
        ssl_context.set_ciphers('ECDHE+AESGCM:!ECDSA')

        environment = os.environ.get('ENV', 'LOCAL')

        if environment == 'LOCAL':
            url = f'amqp://{rabbitmq_user}:{rabbitmq_password}@127.0.0.1:5672'
            parameters = pika.URLParameters(url)
        else:
            url = f'amqps://{rabbitmq_user}:{rabbitmq_password}@{rabbitmq_broker_id}.mq.{region}.amazonaws.com:5671'
            parameters = pika.URLParameters(url)
            parameters.ssl_options = pika.SSLOptions(context=ssl_context)

        self.connection = pika.BlockingConnection(parameters)
        self.channel = self.connection.channel()
