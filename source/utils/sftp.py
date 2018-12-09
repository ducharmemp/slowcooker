import os
import paramiko
# from multiprocessing import

from source.config import CONFIG


t = paramiko.Transport((CONFIG['sftp']['transport']['hostname'], CONFIG['sftp']['transport']['port']))
t.connect(
    **CONFIG['sftp']['auth']
)

# os.register_at_fork(t.atfork)

sftp = paramiko.SFTPClient.from_transport(t)
