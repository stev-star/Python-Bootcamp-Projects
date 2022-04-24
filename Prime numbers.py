num=int(input('Enter a number:'))

def prime(num):
    
    for j in range(2,num):
        if num%j==0:
            print(f'{num} is not a prime number!')
            break
    else:
        print(f'{num} is a prime number')
        
prime(num)
        
