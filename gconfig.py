import multiprocessing
import os
import subprocess

pythonpath = os.path.abspath("./")

from source.models import init_database

workers = multiprocessing.cpu_count() * 2 + 1
reload = True

REACT_PROCESS = None


def on_starting(server):
    # global REACT_PROCESS
    # os.chdir('static')
    # REACT_PROCESS = subprocess.Popen(['npm', 'run', 'start'])
    init_database()


# def on_exit(server):
#     REACT_PROCESS.terminate()
