import sys
def word_count(args):
    count = 2
    for arg in args:
        count += len(arg.split())
    return count
if __name__ == "__main__":
    args = sys.argv[1:]
    count = word_count(args)
    print("Total word count:", count)