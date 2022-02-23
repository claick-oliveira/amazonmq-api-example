from utils.client import Client
import time


class MessageSender(Client):

    def declare_queue(self, queue_name):
        """
        This function declares the queue in RabbitMQ.

        Parameters

        queue_name: The queue name to be declared.

        Output

        Trying to declare queue(<QUEUE NAME>)...
        """
        try:
            print(f"Trying to declare queue({queue_name})...")
            self.channel.queue_declare(queue=queue_name)
            return True
        except Exception:
            return Exception

    def send_message(self, exchange, routing_key, body):
        """
        This function sends message to RabbitMQ.

        Parameters

        exchange: The message routing agents, defined
                  by the virtual host within RabbitMQ
        routing_key: The queue name
        body: The message

        Output

        Sent message. Exchange:
            <EXCHANGE> , Routing Key: <QUEUE NAM>, Body: <MESSAGE>
        """
        try:
            channel = self.connection.channel()
            channel.basic_publish(exchange=exchange,
                                  routing_key=routing_key,
                                  body=body)
            print(
                f"Sent message. Exchange: {exchange}, \
                Routing Key: {routing_key}, Body: {body}")
            return True
        except Exception:
            return Exception

    def close(self):
        """
        This function closes the channel/connection with RabbitMQ.
        """
        try:
            self.channel.close()
            self.connection.close()
            return True
        except Exception:
            return Exception


class MessageReceiver(Client):

    def get_message(self, queue):
        """
        This function declares the queue in RabbitMQ.

        Parameters

        queue: The queue name.

        Output

        Trying to declare queue(<QUEUE NAME>)...
        """
        try:
            method_frame, header_frame, body = self.channel.basic_get(queue)
            if method_frame:
                print(method_frame, header_frame, body)
                self.channel.basic_ack(method_frame.delivery_tag)
                return method_frame, header_frame, body
            else:
                print('No message returned')
            return True
        except Exception:
            return Exception

    def consume_messages(self, queue):
        """
        This function consumes messages from the RabbitMQ.

        Parameters

        queue: The queue name.

        Output

        [*] Waiting for messages. To exit press CTRL+C
        """
        try:
            def callback(ch, method, properties, body):
                time.sleep(1)
                print(" [x] Received %r" % body)

            self.channel.basic_consume(
                queue=queue,
                on_message_callback=callback,
                auto_ack=True
            )

            print(' [*] Waiting for messages. To exit press CTRL+C')
            self.channel.start_consuming()
        except Exception:
            return Exception

    def close(self):
        """
        This function closes the channel/connection with RabbitMQ.
        """
        try:
            self.channel.close()
            self.connection.close()
            return True
        except Exception:
            return Exception
