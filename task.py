# Find the sum of all prime numbers between 20 and 150.

# sum=0
# for i in range(20,151,1):
#     n=i
#     factor=0
#     for j in range(1,n+1,1):
#         if n%j==0:
#             factor=factor+1
#     if factor==2:
#         sum=sum+n      
# print(sum)        

# 2 question  
# Find the average of all perfect numbers between 1 and 1000.      

# count=0
# total=0
# for j in range(1,1001,1):
#     n=j
#     sum=0 
#     for i in range(1,n,1):
#         if n%i==0:
#             sum+=i
#     if sum==n:
#         total=total+n
#         count+=1
# avg=total/count
# print(avg)        



#  3
# Print all leap years between 1900 and 2026

# for i in range(1900,2026+1):
#     if (i%400==0 or (i%4==0 and i%100!=0)):
#         print(i)



#  4 
# Print all palindrome numbers between 100 and 500.


# for i in range(100,501):
#     n=i
#     temp=n
#     rev=0
#     while temp>0:
#         digit=temp%10
#         rev=rev*10+digit
#         temp=temp//10
#     if n==rev:    
#         print(rev)    

# Print all numbers between 120 and 850 whose digit sum is exactly 10.

# for i in range(120,850):
#     num=i
#     temp=num
#     sum=0
#     while temp>0:
#         digit=temp%10
#         temp=temp//10
#         sum=sum+digit
#     if sum==10:
#         print(num,end=" ")
# print()       

# 7
# Print all numbers between 10 and 300 that have exactly 3 factors.

# sum=0
# for i in range(10,301,1):
#     n=i
#     factor=0
#     for j in range(1,n+1,1):
#         if n%j==0:
#             factor=factor+1
#     if factor==3:       
#         print(n)        


# 9
# Print all Armstrong numbers between 100 and 999.

# for i in range(100,1000,1):
#     num=i
#     sum=0
#     temp=num
#     while temp>0:
#         digit=temp%10
#         sum=sum+(digit**3)
#         temp=temp//10
#     if sum==num:
#         print(num)    

# Find the number between 50 and 150 that has the maximum number of factors.

# max_count=0
# for i in range(50,151,1):
#     n=i
#     factor=0
#     for j in range(1,n+1,1):
#         if n%j==0:
#             factor=factor+1
#     print(factor,end=" ")    
#     if factor > max_count:
#         max_count=factor
#         max_number=n        
# print(max_number)                      




