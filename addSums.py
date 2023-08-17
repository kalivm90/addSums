import sys 

def findSums(k, n):
    def combinations(k, n, current_combo):
        if k == 0 and n == 0:
            return [current_combo]
        if k == 0 or n < 0:
            return []

        result = []
        for i in range(n + 1):
            new_combo = current_combo + [i]
            result += combinations(k - 1, n - i, new_combo)
        return result

    return combinations(k, n, [])


def main(): 
    argv = sys.argv 
    argc = len(argv)

    if argc != 3:
        print("Usage: python3 addSums.py k n")

    for i in range(1, len(argv)):
        if int(argv[i]) < 0: 
            print(f"Numbers must be positive")
            sys.exit(0)
        elif not argv[i].isdigit(): 
            print(f"{argv[i]} is not a number")
            sys.exit(0)
            
    k = int(argv[1])
    n = int(argv[2])

    arr = findSums(k, n)
    print(arr)


if __name__ == "__main__": 
    main()