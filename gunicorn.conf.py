import os
import multiprocessing

timeout = 60
bind = os.getenv('SV_BIND')
workers = multiprocessing.cpu_count() * 2 + 1