processes = [1,2,3]
burst = [5,7,4]
quantum = 2

remaining = burst[:]
time = 0

while any(t > 0 for t in remaining):
    for i in range(len(processes)):
        if remaining[i] > 0:
            execute = min(quantum, remaining[i])
            time += execute
            remaining[i] -= execute
            print(f"P{processes[i]} executed for {execute}, Time = {time}")