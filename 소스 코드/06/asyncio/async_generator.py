###################################
# File Name : async_generator.py (Python 3.6 or later)
###################################
#!/usr/bin/python3

import asyncio

async def delay_range(to, delay=1):
    for i in range(to):
        yield i
        await asyncio.sleep(delay)

async def run():
    async for i in delay_range(10):
        print (i)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(run())
    finally:
        loop.close()
