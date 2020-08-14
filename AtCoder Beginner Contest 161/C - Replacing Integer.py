N,K = map(int, input().split())
N = N%K
absolute = abs(K-N)
print(absolute if absolute < N else N)
