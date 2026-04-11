import os
pid = os.fork()  # Creates a child process
if pid == 0:
    print("Child Process – PID:", os.getpid())
else:
    print("Parent Process – PID:", os.getpid())
