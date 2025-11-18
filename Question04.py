# Print numbers from N to 1

def print_reverse(N):
    if N == 0:
        return
    print(N, end=" ")
    print_reverse(N - 1)

N = int(input())
print_reverse(N)