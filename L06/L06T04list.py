"""Five judges are used in hill jumping.
Each gives the jump a score from one to twenty 1-20.Write a 
program that asks for the evaluation points for one jump and 
prints the sum of the style points in such a way that the 
smallest and largest style points have been subtracted from the sum. """
number_of_judges = 5
sum = 0
list = []
# Using for loop to iterate till the range
for i in range(5):
    # asking user input
    score = input("jump score from 1 to 20: ")
    if score=='':
        break
    elif int(score)>20 or int(score)<1:     # check condition score shd be 1 to 20
            print('Invalid input. Score couldn\'t be zero,negative or higher')
            score = input("jump score: ")    # reasking score for wrong entry
    
    list.append(int(score))     # append the score value in list
    sum+=int(score)             # sum of score values 
print(list)
highest = max(list)
lowest = min(list)
total_points = sum - (highest + lowest)
print("score total:",total_points)