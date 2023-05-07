import sys
import itertools

input = sys.stdin.readline

n, k = map(int, input().split())

if k < 5:
    print(0)
else:
    letters = set(['a', 'c', 'i', 'n', 't'])
    learned = set()
    word = []
    cnt = 0

    for _ in range(n):
        word.append(set(input().rstrip()[4:-4]) - letters)

    for comb in itertools.combinations(set.union(*word), min(k-5, len(set.union(*word)))):
        learned_set = set(comb).union(letters)
        cnt_comb = 0
        for i in word:
            if i.issubset(learned_set):
                cnt_comb += 1
        cnt = max(cnt, cnt_comb)

    print(cnt)