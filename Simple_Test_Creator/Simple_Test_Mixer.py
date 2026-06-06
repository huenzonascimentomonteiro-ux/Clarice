# Open the two files and create one variable for everyone with the content of it.
with open("Test_1.txt") as f1:
    final_test = f1.read()
 
with open("Test_2.txt") as f2:
    final_test = f2.read() 

# Transform the text into lines
lines = final_test.splitlines() 

# Have the program create questions using the content of the odd-numbered row and check if it is correct in relation to the content of the even-numbered row.
## Question 1  # 0
## Answer 1    # 1
## Question 2  # 2
## Answer 2    # 3

i = 0

right_answer = 0
wrong_answer = 0

while i < len(lines):
    Question = input(lines[i] + " ")

    if Question == lines[i + 1] :
        print("Right answer!!!")
        right_answer += 1
    else:
        print("Wrong Answer!!!")
        wrong_answer += 1
    
    i += 2
    

if i == len(lines):
    print (f"Right:{right_answer}" + " | " + f"Wrong:{wrong_answer}")
