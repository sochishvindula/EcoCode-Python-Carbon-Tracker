from ecocode import eco_monitor

@eco_monitor
def fibonacci_example(n):
    """Example showing EcoCode monitoring Fibonacci calculation"""
    if n <= 1:
        return n
    return fibonacci_example(n-1) + fibonacci_example(n-2)

if __name__ == "__main__":
    print("🧮 Testing Fibonacci with EcoCode monitoring")
    result = fibonacci_example(10)
    print(f"Result: {result}")
