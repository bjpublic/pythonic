###################################
# File Name : native_coroutine_with_task.py (Python 3.5 or later)
###################################
#!/usr/bin/python3

import asyncio
import random
import datetime

async def print_time(idx):
    sleep_time = random.randrange(1, 5)
    await asyncio.sleep(sleep_time)
    print ("[%s] Sleep time : %s, Complete time : %s" % (idx, sleep_time, datetime.datetime.now()))
    return idx

async def tasks():
    task_list = [asyncio.ensure_future(print_time(i)) for i in range(10)]

    for idx, task in enumerate(task_list):
        if idx % 2 == 0:
            task.cancel()
            print ("[%s] task is cancelled" % idx)
        else:
            task.add_done_callback(callback)

    await asyncio.wait(task_list)

def callback(task):
    print ("[%s] Call callback function" % task.result())

def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(tasks())
    loop.close()


if __name__ == "__main__":
    main()
