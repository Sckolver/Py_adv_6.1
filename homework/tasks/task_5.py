import asyncio
from typing import Coroutine


async def limit_execution_time(coro: Coroutine, max_execution_time: float) -> None:
    # Функция принимает на вход корутину, которую необходимо запустить, однако иногда она выполняется
    # слишком долго, это время необходимо ограничить переданным на вход количеством секунд.
    #
    # Тест проверяет, что каждая переданная корутина была запущена, и все они завершились за заданное
    # время.

    task = asyncio.create_task(coro)
    try:
        await asyncio.wait_for(task, timeout=max_execution_time)
    except asyncio.TimeoutError:
        task.cancel()
        try:
            await task
        except asyncio.CancelledError:
            pass


async def limit_execution_time_many(*coros: Coroutine, max_execution_time: float) -> None:
    # Функция эквивалентна limit_execution_time, но корутин на вход приходит 
    # несколько.
    tasks = [asyncio.create_task(c) for c in coros]
    try:
        await asyncio.wait_for(asyncio.gather(*tasks),
                               timeout=max_execution_time)
    except asyncio.TimeoutError:
        for t in tasks:
            t.cancel()
        await asyncio.gather(*tasks, return_exceptions=True)