import asyncio
from dataclasses import dataclass
from typing import Awaitable


@dataclass
class Ticket:
    number: int
    key: str


async def coroutines_execution_order(coros: list[Awaitable[Ticket]]) -> str:
    # Необходимо выполнить все полученные корутины, затем упорядочить их
    # результаты по полю number и вернуть строку, состоящую из склеенных полей key.
    results = await asyncio.gather(*coros)
    results.sort(key=lambda t: t.number)
    return ''.join(ticket.key for ticket in results)
