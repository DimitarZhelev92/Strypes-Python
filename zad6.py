def is_decreasing(n):
        return (all(n[i] >= n[i + 1] for i in range(len(n) - 1)))
n = [100, 50, 20]
print(is_decreasing(n))
