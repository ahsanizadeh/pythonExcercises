#Exercise Question 1: Print First 10 natural numbers using while loop
#for i in range(11):
#    print(i)

# Exercise Question 2: Print the following pattern
# pattern = []
# i = 1
# while i < 6:
#     pattern.append(i)
#     print(' '.join(str(e) for e in pattern))
#    i += 1

#Exercise Question 4: Print multiplication table of given number
# def multiplication(num):
#     for i in range(1,11):
#         print(num*i)
    
# multiplication(2)

#Exercise Question 5: Given a list iterate it and display numbers which are divisible by 5 and if you find number greater than 150 stop the loop iteration
list1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
for e in list1:
    if e % 5 == 0:
        if e > 150:
            break
        print(e)
           