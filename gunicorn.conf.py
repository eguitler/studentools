import os
import multiprocessing

bind = os.getenv('SV_BIND')
workers = multiprocessing.cpu_count() * 2 + 1