import asyncio
import logging
import sys

from index import start

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)
    try:
        asyncio.run(start())
    except KeyboardInterrupt:
        print('KeyboardInterrupt')
