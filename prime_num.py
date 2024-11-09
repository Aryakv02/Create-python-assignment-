def find_primes(start, end):
    for num in range(start, end + 1):
        if num > 1:
            for i in range(2, int(num**0.5) + 1):
                if (num % i) == 0:
                    break
            else:
                print(num)
                

if __name__ == "__main__":
    
   start = int(input("Enter the start of the range: "))
   end = int(input("Enter the end of the range: "))

   print("Prime numbers between", start ,"and",end,":")
   find_primes(start,end)
 