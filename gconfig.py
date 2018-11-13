import multiprocessing
import os
import subprocess

pythonpath = os.path.abspath("./")

workers = multiprocessing.cpu_count() * 2 + 1
reload = True

REACT_PROCESS = None


def on_starting(server):
    global REACT_PROCESS
    REACT_PROCESS = subprocess.Popen(['npm', 'run', 'start', '--prefix', './source/public/'])

def on_exit(server):
    REACT_PROCESS.terminate()
