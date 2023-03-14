import asyncio


async def say1():
    await asyncio.sleep(1)
    print("Hello 1!")


async def say2():
    await asyncio.sleep(1)
    print("Hello 2!")

# This code valid till Python3.10
# loop = asyncio.get_event_loop()
# loop.run_until_complete(asyncio.gather(
#     say1(),
#     say2()
# ))


# This code is for Python3.11
async def main():
    await asyncio.gather(say1(), say2())

asyncio.run(main())
