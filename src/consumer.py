import os, sys, json, random
from utils.client import Client

class MessageReceiver(Client):

    def get_message(self, queue):
        """
        This function declares the queue in RabbitMQ.

        Parameters

        queue: The queue name.

        Output

        Trying to declare queue(<QUEUE NAME>)...
        """
        method_frame, header_frame, body = self.channel.basic_get(queue)
        if method_frame:
            print(method_frame, header_frame, body)
            self.channel.basic_ack(method_frame.delivery_tag)
            return method_frame, header_frame, body
        else:
            print('No message returned')

    def consume_messages(self, queue):
        """
        This function consumes messages from the RabbitMQ.

        Parameters

        queue: The queue name.

        Output

        [*] Waiting for messages. To exit press CTRL+C
        """
        def callback(ch, method, properties, body):
            print(" [x] Received %r" % body)

        self.channel.basic_consume(queue=queue, on_message_callback=callback, auto_ack=True)

        print(' [*] Waiting for messages. To exit press CTRL+C')
        self.channel.start_consuming()

    def close(self):
        """
        This function closes the channel/connection with RabbitMQ.
        """
        self.channel.close()
        self.connection.close()

if __name__ == "__main__":

    # Get the path name
    pathname = os.path.dirname(sys.argv[0])

    if os.path.isfile(f'{pathname}/../config.json'):
      # Opening JSON file
      f = open(f'{pathname}/../config.json')

      # returns JSON object as a dictionary
      data = json.load(f)

      # Closing file
      f.close()

    else:
        print ("The config.json not exist! Check with you create the file based on the config.json.template file.")

    # Create Basic Message Receiver which creates a connection
    # and channel for consuming messages.
    basic_message_receiver = MessageReceiver(
        data["broker-id"],
        data["username"],
        data["password"],
        data["region"]
    )

    # Consume the message that was sent.
    #basic_message_receiver.get_message(data["queue"])

    # Consume multiple messages in an event loop.
    basic_message_receiver.consume_messages(data["queue"])

    # Close connections.
    basic_message_receiver.close()
