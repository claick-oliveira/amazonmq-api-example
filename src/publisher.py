import os, sys, json, random
from utils.client import Client

class MessageSender(Client):

    def declare_queue(self, queue_name):
        """
        This function declares the queue in RabbitMQ.

        Parameters

        queue_name: The queue name to be declared.

        Output

        Trying to declare queue(<QUEUE NAME>)...
        """
        print(f"Trying to declare queue({queue_name})...")
        self.channel.queue_declare(queue=queue_name)

    def send_message(self, exchange, routing_key, body):
        """
        This function sends message to RabbitMQ.

        Parameters

        exchange: The message routing agents, defined by the virtual host within RabbitMQ
        routing_key: The queue name
        body: The message

        Output

        Sent message. Exchange: <EXCHANGE> , Routing Key: <QUEUE NAM>, Body: <MESSAGE>
        """
        channel = self.connection.channel()
        channel.basic_publish(exchange=exchange,
                              routing_key=routing_key,
                              body=body)
        print(f"Sent message. Exchange: {exchange}, Routing Key: {routing_key}, Body: {body}")

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

    # Initialize Basic Message Sender which creates a connection
    # and channel for sending messages.
    basic_message_sender = MessageSender(
        data["broker-id"],
        data["username"],
        data["password"],
        data["region"]
    )

    # Load the data
    f = open(f'{pathname}/utils/unicorns.json')

    # returns JSON object as a dictionary
    unicorns = json.load(f)

    # Closing file
    f.close()

    # Get random unicorn
    unicorn = random.choice(unicorns)

    # Declare a queue
    basic_message_sender.declare_queue(data["queue"])

    # Send a message to the queue.
    basic_message_sender.send_message(exchange="", routing_key=data["queue"], body=json.dumps(unicorn))

    # Close connections.
    basic_message_sender.close()
