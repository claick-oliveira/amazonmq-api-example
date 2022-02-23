import os
import sys
import json
from rmq_conn import MessageReceiver

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
        print("The config.json not exist! Check with you create the \
              file based on the config.json.template file.")

    # Create Basic Message Receiver which creates a connection
    # and channel for consuming messages.
    basic_message_receiver = MessageReceiver(
        data["broker-id"],
        data["username"],
        data["password"],
        data["region"]
    )

    # Consume the message that was sent.
    # basic_message_receiver.get_message(data["queue"])

    # Consume multiple messages in an event loop.
    basic_message_receiver.consume_messages(data["queue"])

    # Close connections.
    basic_message_receiver.close()
