import asyncio
from dataclasses import dataclass

from py_skeleton.logger import logger


@dataclass
class MyService:
    name: str

    async def compute(self) -> bool:
        await asyncio.sleep(1)
        logger.debug(f"Computed for service {self.name}")
        return True
