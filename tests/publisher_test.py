from unittest.mock import patch
from src.publisher import MessageSender
import os
import sys
import json
import random


@patch.dict(os.environ, {
    'ENV': 'LOCAL'
})
def test_publish_message():
    # Get the path name
    pathname = os.path.dirname(sys.argv[0])

    # Initialize Basic Message Sender which creates a connection
    # and channel for sending messages.
    basic_message_sender = MessageSender(
        "broker-id",
        "mock",
        "mock",
        "region"
    )

    # Load the data
    f = open(f'{pathname}/../../../src/utils/unicorns.json')

    # returns JSON object as a dictionary
    unicorns = json.load(f)

    # Closing file
    f.close()

    # Get random unicorn
    unicorn = random.choice(unicorns)

    # Declare a queue
    basic_message_sender.declare_queue('mock')

    # Send a message to the queue.
    basic_message_sender.send_message(
        exchange="", routing_key='mock', body=json.dumps(unicorn))

    # Close connections.
    basic_message_sender.close()
