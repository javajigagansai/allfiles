def toh(n, source, auxiliary, target):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    toh(n - 1, source, target, auxiliary)
    print(f"Move disk {n} from {source} to {target}")
    toh(n - 1, auxiliary, source, target)

if __name__ == "__main__":
    n = int(input("Enter the number of disks: "))
    toh(n, 'A', 'B', 'C')
