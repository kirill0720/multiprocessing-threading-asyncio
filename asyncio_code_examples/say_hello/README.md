# Parallel execution of asyncio functions

This document explains how Python's asyncio library can be used for parallel execution of asynchronous functions. 
It provides an example of how to start and wait for two async functions to finish using asyncio.

## Code Example

The following code example demonstrates how to start two async functions at the same time and wait until they both finish:

```
import asyncio

async def say1():
    await asyncio.sleep(1)
    print("Hello 1!")

async def say2():
    await asyncio.sleep(1)
    print("Hello 2!")

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.gather(
    say1(),
    say2()
))

```

## Visualization
>Assume that all red lines are at 0s time point, and all blue at 1s

![image](https://s.hinty.io/QGceYMz3mn7jtFENT3CAVE.png)


## Explanation

Asyncio is not multithreading or multiprocessing, but it runs code in parallel. 

When `run_until_complete` runs `say1` function, the interpreter executes it line by line, and when it sees `await`, 
it starts asynchronous operation which later will be finished with some internal callback to loop. 
After the start, it immediately returns control to the event loop. 
So it starts asynchronous sleep and our loop has control, so the loop is actually ready to start the next function `say2`. 

When first async sleep is finished, it makes an internal callback to loop 
and loop resumes execution of `say1` coroutine: next operation is printing `Hello 1!`. 
After printing it returns again to the event loop. 
At the same time, from the second sleep, the loop receives an event about finishing the second sleep. 
So now `Hello 2!` printed and second method also returned. 

`run_until_complete(gather(l1,l2,l3))` will block until all `l1`, `l2`, `l3` coroutines will be done.