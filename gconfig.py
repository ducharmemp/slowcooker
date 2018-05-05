import multiprocessing
import os

pythonpath = os.path.abspath("./")

workers = multiprocessing.cpu_count() * 2 + 1
reload = True
