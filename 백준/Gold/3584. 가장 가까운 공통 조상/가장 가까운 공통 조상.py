import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
  n = int(input())
  parents = [0 for _ in range(n+1)]
  for _ in range(n-1):
    parent, child = map(int, input().split())
    parents[child] = parent # 부모 저장

  a, b = map(int, input().split())
  a_parent = [a]
  b_parent = [b]
  # 각 노드의 부모 노드가 루트일 때까지 모두 저장
  while parents[a]:
    a_parent.append(parents[a])
    a = parents[a]
    
  while parents[b]:
    b_parent.append(parents[b])
    b = parents[b]  
  # 같은 에벨로 맞추고 부모 노드 같은 것 찾기
  a_lev = len(a_parent)-1
  b_lev = len(b_parent)-1
  # 루트 노드 부터 차례대로 비교
  while a_parent[a_lev] == b_parent[b_lev]:
    a_lev -= 1
    b_lev -= 1
  
  print(a_parent[a_lev+1])