#!/usr/bin/env python3
""" 2-measure runtime module """
import asyncio
from time import perf_counter
wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """ a measure_time function with integers n and
    max_delay as arguments that measures the total execution
    time for wait_n(n, max_delay), and returns
    total_time / n. Your function should return a float"""

    start_time = perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end_time = perf_counter() - start
    return end_time / n
