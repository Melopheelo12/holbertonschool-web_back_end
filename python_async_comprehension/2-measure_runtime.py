#!/usr/bin/env python3
"""Module with a coroutine that measures runtime of running
async_comprehension four times in parallel.
"""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Execute async_comprehension four times in parallel using
    asyncio.gather, measure and return the total runtime.
    """
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.time() - start_time
