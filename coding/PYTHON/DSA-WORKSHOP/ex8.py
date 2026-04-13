n = 5
queue = []
front = 0
rear = 0
j = 1
print("Priority Queue using array:")
print("-------------------------------------------------------------------")
while True:
print("\n1. Insertion\n2. Deletion\n3. Display (sorted)\n4. Exit")
ch = int(input("Enter your choice: "))
if ch == 1:
if rear == n:
print("The queue is full.")
else:
value = int(input(f"Enter value {j}: "))
queue.append(value)
rear += 1
j += 1
elif ch == 2:
if front == rear:
print("Queue is empty.")
else:
deleted = queue.pop(0)
print(f"The deleted element is {deleted}")
rear -= 1
elif ch == 3:
if front == rear:
print("No elements in queue to be shown.")
else:
print("The sorted queue elements are:")
sorted_queue = sorted(queue) # Sorting the queue
for elem in sorted_queue:
print(elem, end=" ")
print()
elif ch == 4:
print("Exit")
break
else:
print("Invalid option")