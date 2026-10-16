# Problem 16: Nested Lists
# https://www.hackerrank.com/challenges/nested-list/problem

if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])
    second_lowest = sorted(set(score for _, score in records))[1]
    for name in sorted(n for n, s in records if s == second_lowest):
        print(name)
