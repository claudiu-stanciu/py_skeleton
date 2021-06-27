import asyncio

from py_skeleton.logger import logger
from py_skeleton.service import MyService


async def main():
    logger.info("Hello world ")
    service = MyService("test")
    await service.compute()


if "__name__" == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
