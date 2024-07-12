#!/usr/bin/env python3
""" 2-measure runtime module """
from typing import List
import time
import asyncio
import importlib.util


module_path = './1-concurrent_coroutines.py'

spec = importlib.util.spec_from_file_location('module_name', module_path)
module = importlib.util.module_from_spec(spec)

spec.loader.exec_module(module)

wait_n = module.wait_n
