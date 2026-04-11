import queue
q = queue.Queue(5)
def producer():
    for i in range(5):
        q.put(i)
        print("Produced:", i)
def consumer():
    while not q.empty():
        print("Consumed:", q.get())
producer()
consumer()