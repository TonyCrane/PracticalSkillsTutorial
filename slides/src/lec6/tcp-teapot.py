#!/usr/bin/env python3

# socat TCP-LISTEN:39200,reuseaddr,fork EXEC:"python3 tcp-teapot.py"

import re
import sys
import select
import signal
import random
from datetime import datetime, UTC


PORT = 39200
SECONDS = random.randint(10, 60)
DATE_BEFORE = datetime(2024, 5, 17, 19, 30, 0)


def alarm_handler(signum, frame):
    print('Time is up! Closing up...', flush=True)
    exit(0)


message = f"""===== PRACTICAL SKILLS TUTORIAL: LECTURE 6 =====

Hello! This is a TCP server hosted on port {PORT}.
Seeing this message means that """

if datetime.now() < DATE_BEFORE:
    message += 'your nc / ncat is working properly.'
    print(message, flush=True)
    exit(0)
else:
    message += 'you have successfully connected to the server.\n'

# https://stackoverflow.com/a/2904057/12499162
# try to read a line without blocking
# if it works, it means something (very likely a browser) has already
# connected and sent a message (very likely an HTTP request)
i, _, _ = select.select([sys.stdin], [], [], 0)

if i:
    # probably on a browser, find host header
    # ignore those who don't send host header, might be `echo` piped to `nc`
    # somewhat like isatty() but not really
    try:
        while True:
            line = input().lower()
            if line.startswith('host:'):
                host = line.split(' ')[1]
                if PORT != 80:
                    host = host.rsplit(':', 1)[0]
                break
            elif not line:
                # empty line, end of headers
                raise EOFError
    except EOFError:
        exit(0)

    if host.startswith('['):
        # it's an IPv6 address, remove brackets
        host = host[1:-1]

    message += f"""
However, it appears that you are on a browser, which means, nothing much fun to see here.
Try using a terminal instead:

\tnc {host} {PORT}"""

    if random.randint(1, 5) == 1:
        # random teapot
        message = message.replace('server', 'teapot')

    message = message.strip().replace('\n', '\r\n') + '\r\n'

    header = f"""HTTP/1.1 418 I'm a teapot
Content-Type: text/plain; charset=UTF-8
Cache-Control: no-cache
Server: Python/{sys.version.split()[0]}
Content-Length: {len(message)}
Date: {datetime.now(UTC).strftime('%a, %d %b %Y %H:%M:%S GMT')}
Connection: close
""".replace('\n', '\r\n')

    print(header, end='\r\n')
    print(message, end='', flush=True)

else:
    message += f"""Better yet, you are using a terminal to connect to this server!
Try sending a message to the server. The server will acknowledge your message.
Send Ctrl-C to end the connection.
Send Ctrl-D (on Unix) to send an EOF, which will also end the connection.
This connection will close in {SECONDS} seconds!
"""

    print(message, flush=True)
    counter = 0
    signal.signal(signal.SIGALRM, alarm_handler)
    signal.alarm(SECONDS)

    flag_pattern = re.compile(r'^cat\s+/?flag|\.?/readflag$')

    try:
        while True:
            message = input().strip()
            counter += 1

            if flag_pattern.fullmatch(message):
                print('You have found the easter egg! flag{1\'m_a_t3ap0t}')
            else:
                print(f'Server acknowledged your message #{counter}: {message}')
            print(flush=True)
    except EOFError:
        pass
