def digits_recursive(n, digits=[]): 
    return digits_recursive(n // 10, [n % 10] + digits) if n else digits or [0]
    digits_recursive(123)
input()