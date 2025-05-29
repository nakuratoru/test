import matplotlib.pyplot as plt

# Compute Fibonacci sequence
def fibonacci(n):
    seq = [0, 1]
    for i in range(2, n):
        seq.append(seq[-1] + seq[-2])
    return seq[:n]

if __name__ == "__main__":
    n = 10
    seq = fibonacci(n)
    plt.plot(range(n), seq, marker='o')
    plt.title('Fibonacci Sequence')
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.grid(True)
    plt.show()
