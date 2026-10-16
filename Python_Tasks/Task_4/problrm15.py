# Problem 15: Word Order
# https://www.hackerrank.com/challenges/word-order/problem

if __name__ == '__main__':
    n = int(input())
    counts = {}  # dicts keep insertion order
    for _ in range(n):
        word = input().strip()
        counts[word] = counts.get(word, 0) + 1
    print(len(counts))
    print(*counts.values())
