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

# Initialize counters for each category
fail = 0
pAss = 0 
good = 0
excellent = 0

# Loop to continously accept scores
while True:
    # Categorize the score
    student_scores = int(input("Enter a student score (negative number to stop): "))
    if 0 <= student_scores < 50:
        print("Fail")
        fail += 1
    elif 50 <= student_scores <= 69:
        print("Pass")
        pAss += 1
    elif 70 <= student_scores <= 89:
        print("Good")
        good += 1
    elif 90 <= student_scores <= 100:
        print("Excellent")
        excellent += 1
    # Print the final counts when the loop is stopped
    elif student_scores < 0:
        print(f"There were {excellent} excellent scores, {good} good scores, {pAss} passing scores, and {fail} failing scores.")
        break
    else:
        print("Invalid score. Please enter a score between 0 and 100.")







# Problem 2: Even and Odd Counter with Conditions
    # Ask the user for a starting and ending number.
    # Use a for loop to iterate from the starting to the ending number.
    # Inside the loop:
        # Use nested if to check if the number is both even and greater than 10. If true, count it as a "special even" number.
        # If it's odd and less than 20, count it 
        # as a "special odd" number.
# Print the counts for both "special even" and "special odd" numbers.
    
# Prompt the user for starting and ending numbers
start = int(input("Enter a starting number: "))
end = int(input("Enter an ending number: "))

# Initialize counters for special even and special odd numbers
special_even_count = 0
special_odd_count = 0

# Loop through the range from start to end (inclusive)
for num in range(start, end + 1):
    if num % 2 == 0 and num > 10: # Check for special even
        print(f'{num} is a Special Even')
        special_even_count += 1
    elif num % 2 != 0 and num < 20: # Check for special odd
        print(f'{num} is a Special Odd')
        special_odd_count += 1

# Print the total counts
print("\nCounts:")
print(f"Special Even numbers: {special_even_count}")
print(f"Special Odd numbers: {special_odd_count}")