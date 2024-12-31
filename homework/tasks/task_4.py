async def coroutines_execution_order(i: int = 42) -> int:
    order = []

    async def task_1(x: int):
        order.append('1')
        if x == 0:
            return
        if x > 5:
            await task_2(x // 2)
        else:
            await task_2(x - 1)

    async def task_2(x: int):
        order.append('2')
        if x == 0:
            return
        if x % 2 == 0:
            await task_1(x // 2)
        else:
            await task_2(x - 1)

    await task_1(i)

    return int(''.join(order))
