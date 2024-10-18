def is_num_in_fibonacci(num):
    a = 0
    b = 1

    if (n==a or n==b):
        return True
    
    while True:
        c=b
        b=a+b
        a=c
        if b==num:
            return True
        elif b > num:
            return False
    
n = int(input("Insira um número: "))

if is_num_in_fibonacci(n):
    print(f"O numero {n} pertence a sequência de Fibonacci")
else:
    print(f"O numero {n} não pertence a sequência de Fibonacci")
