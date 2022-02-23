import os
import sys
import json
import random
from rmq_conn import MessageSender

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
        print("The config.json not exist! Check with you create the file \
               based on the config.json.template file.")

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
    basic_message_sender.send_message(
        exchange="", routing_key=data["queue"], body=json.dumps(unicorn))

    # Close connections.
    basic_message_sender.close()
