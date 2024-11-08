# Anabel Perez & Ruby Solis-Chavez
# Problem 1: Student Grade Categorization
# Ask the user to enter a list of student scores (one by one).
# Use a while loop to continuouly accept scores until the user enters a negative number.
# For each score, use nested if statements to categorize the score:
#   90-100: Print "Excellent"
#   70-89: Print "Good"
#   50-69: Print "Pass"
#   Below 50: Print "Fail"
# Stop the loop and print the final count of each category when the user enters a negative number.

student_scores = int(input("Enter a student score: "))
fail = 0
pAss = 0 
good = 0
excellent = 0
while True:
    if 0<student_scores<=50:
        print("Fail")
        fail += 1
    elif 50< student_scores <= 69:
        print("Pass")
        pAss += 1
    elif 70< student_scores <= 89:
        print("Good")
        good += 1
    elif 90< student_scores <= 100:
        print("Excellent")
        excellent += 1
    elif student_scores <0:
        print(f"There were {excellent} excellent scores, {good} good scores, {pAss} passing scores, and {fail} failing scores.")
        break
        
    student_scores = int(input("Enter a student score: "))






# Problem 2: Even and Odd Counter with Conditions
    # Ask the user for a starting and ending number.
    # Use a for loop to iterate from the starting to the ending number.
    # Inside the loop:
        # Use nested if to check if the number is both even and greater than 10. If true, count it as a "special even" number.
        # If it's odd and less than 20, count it 
        # as a "special odd" number.
# Print the counts for both "special even" and "special odd" numbers.
    

start = int(input("Enter a starting number: "))
end = int(input("Enter an ending number: "))
for num in range(start, end):
    if num%2==0 and num >= 10:
        print("Special Even")
    else:
        print("Special Odd")
