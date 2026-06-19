#!/usr/bin/env python3

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int):
    attend = wait_random(max_delay)
    return asyncio.ensure_future(attend)
