A, B = map(int, input().split())
C = list(map(int, input().split()))

max_height = [0] * A

for i in range(B):
    a, b = map(int, input().split())
    max_height[a - 1] = max(max_height[a - 1], C[b - 1])
    max_height[b - 1] = max(max_height[b - 1], C[a - 1])

print((sum(C[i] > max_height[i] for i in range(A))))