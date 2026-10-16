# Problem 18: Lists
# https://www.hackerrank.com/challenges/python-lists/problem

if __name__ == '__main__':
    n = int(input())
    arr = []
    for _ in range(n):
        cmd, *args = input().split()
        args = list(map(int, args))
        if cmd == "insert":
            arr.insert(args[0], args[1])
        elif cmd == "print":
            print(arr)
        elif cmd == "remove":
            arr.remove(args[0])
        elif cmd == "append":
            arr.append(args[0])
        elif cmd == "sort":
            arr.sort()
        elif cmd == "pop":
            arr.pop()
        elif cmd == "reverse":
            arr.reverse()
