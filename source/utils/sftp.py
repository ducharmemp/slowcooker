import os
import paramiko
from multiprocessing.util import register_after_fork

from source.config import CONFIG


t = paramiko.Transport((CONFIG['sftp']['transport']['hostname'], CONFIG['sftp']['transport']['port']))
t.connect(
    **CONFIG['sftp']['auth']
)

if not hasattr(os, 'register_at_fork'):
    register_after_fork(t, paramiko.Transport.atfork)
else:
    os.register_at_fork(t.atfork)

sftp = paramiko.SFTPClient.from_transport(t)
