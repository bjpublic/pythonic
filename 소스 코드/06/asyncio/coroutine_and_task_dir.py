###################################
# File Name : coroutine_and_task_dir.py (Python 3.5 or later)
###################################
#!/usr/bin/python3

import asyncio
import datetime

async def func(caller):
    print ("Start %s" % caller)
    await asyncio.sleep(3)
    print ("End %s" % caller)
    return "Done"

async def coro():
    c = func("coro")
    print (c)
    print (dir(c))
    ret = await c
    print ("coro ret : %s" % ret)

async def task():
    t = asyncio.ensure_future(func("task"))
    print (t)
    print (dir(t))
    ret = await t
    print ("task ret : %s" % ret)

def callback(future):
    print ("task callback")

def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(coro())
    loop.run_until_complete(task())
    loop.close()


if __name__ == "__main__":
    main()
