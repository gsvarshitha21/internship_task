# Problem 20: No Idea!
# https://www.hackerrank.com/challenges/no-idea/problem

if __name__ == '__main__':
    n, m = map(int, input().split())
    arr = input().split()
    a = set(input().split())
    b = set(input().split())
    happiness = sum((x in a) - (x in b) for x in arr)
    print(happiness)
