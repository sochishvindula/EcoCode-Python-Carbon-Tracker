@eco_monitor
def inefficient_example():
    """I made this to show you what NOT to do"""
    result = []
    for i in range(100000):
        result.append(i ** 2)  # Inefficient: creates new objects repeatedly
    return result

@eco_monitor  
def efficient_example():
    """I optimized this version to show you the difference"""
    return [i ** 2 for i in range(100000)]  # Efficient: list comprehension

@eco_monitor
def your_code_here():
    """Replace this with your own code to see its environmental impact"""
    time.sleep(1)  # Simulating some work
    return "Your code completed!"

if __name__ == "__main__":
    print("🌱 Welcome to EcoCode - I'll help you write greener Python!")
    print("\nI'm testing both efficient and inefficient code so you can see the difference:")
    
    print("\n" + "="*60)
    print("❌ INEFFICIENT VERSION:")
    inefficient_result = inefficient_example()
    
    print("\n" + "="*60) 
    print("✅ EFFICIENT VERSION:")
    efficient_result = efficient_example()
    
    print("\n" + "="*60)
    print("🧪 YOUR CODE TEST:")
    your_result = your_code_here()
    
    print(f"\n🎯 Key Takeaway: I showed you that small changes in how you write")
    print(f"   code can make a big difference in environmental impact!")
    
    print(f"\n💡 Next Steps I Recommend:")
    print(f"   1. Use my @eco_monitor decorator on your functions")
    print(f"   2. Compare different implementations of the same logic") 
    print(f"   3. Optimize functions that show high CO2 emissions")
    print(f"   4. Share your green coding practices with others!")
