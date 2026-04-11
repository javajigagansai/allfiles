import threading
def philosopher(id):
    print(f"Philosopher {id} thinking")
    print(f"Philosopher {id} eating")
threads = []
for i in range(5):
    t = threading.Thread(target=philosopher, args=(i,))
    threads.append(t)
    t.start()