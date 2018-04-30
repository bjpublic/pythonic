###################################
# File Name : async_for.py (Python 3.5 or later)
###################################
#!/usr/bin/python3

import asyncio

class AsynchronousReader:

    def __init__(self, file_name):
        self.file_name = file_name
        self.file = None

        try:
            self.file = open(self.file_name, "rb")
        except:
            print ("File open error.")

    def __aiter__(self):
        return self

    async def __anext__(self):
        value = await self.file_readline()
        if value == b"":
            raise StopAsyncIteration
        return value.decode("utf-8").strip()

    async def file_readline(self):
        return self.file.readline()

    def file_close(self):
        self.file.close()


async def read_file(file_name):
    async_reader = AsynchronousReader(file_name)
    async for value in async_reader:
        print (value)

    async_reader.file_close()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(read_file("./python_foudation_mission_statement"))
    finally:
        loop.close()
