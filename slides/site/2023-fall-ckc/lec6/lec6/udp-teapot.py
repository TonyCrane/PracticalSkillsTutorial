#!/usr/bin/env python3

# socat UDP-RECVFROM:39200,reuseaddr,fork EXEC:"python3 udp-teapot.py"

import random
from datetime import datetime


PORT = 39200

message = f"""
===== PRACTICAL SKILLS TUTORIAL: LECTURE 6 =====

Hello! This is a UDP server hosted on port {PORT}.
Seeing this message means that the server has received a message from you:

\t"{input()}"

Unlike TCP, UDP is connectionless. Every message you send is treated as a separate packet.
Which means, if you send another message, you will see this message again.

The current time is {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}.
Press Ctrl-C to quit."""

if random.randint(1, 5) == 1:
    message = message.replace('server', 'teapot')

print(message)
