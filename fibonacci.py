def fibonacci(n):
    series = [0, 1]
    while len(series) < n:
        series.append(series[-1] + series[-2])
    return series[:n]

# Wait for user input
n = int(input("Enter the number of terms: "))
print(f"Fibonacci series: {fibonacci(n)}")