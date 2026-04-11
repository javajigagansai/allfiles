n = 4
bt = [4, 3, 5, 2]  
wt = [0] * n
tat = [0] * n
for i in range(1, n):
    wt[i] = wt[i-1] + bt[i-1]
for i in range(n):
    tat[i] = bt[i] + wt[i]
print("\nP\tBT\tWT\tTAT")
for i in range(n):
    print(f"P{i+1}\t{bt[i]}\t{wt[i]}\t{tat[i]}")
print("\nAverage WT:", sum(wt)/n)
print("Average TAT:", sum(tat)/n)