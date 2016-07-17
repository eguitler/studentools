import os
import multiprocessing

timeout = os.getenv('SV_TIMEOUT')
bind = os.getenv('SV_BIND')
workers = multiprocessing.cpu_count() * 2 + 1