#!/usr/bin/env python3
"""
a coroutine called async_comprehension
"""

import asyncio as a
from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    A coroutine that takes no arguments.
    The coroutine will collect 10 random numbers using an async comprehensing
    over async_generator, then return the 10 random numbers.
    """
    async_numbers = [number async for number in async_generator()]
    return async_numbers
