import sys
input = sys.stdin.readline
from collections import Counter

n = int(input())
li = [str(input().rstrip()) for _ in range(n)]
best_seller = Counter(li)
max_count = max(best_seller.values())
max_items = [item for item, count in best_seller.items() if count == max_count]
max_items.sort()
print(max_items[0])