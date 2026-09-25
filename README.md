# Tutedude-Assignment-5

Task 1: Create a Dictionary of Student Marks

CODE

#Dictionary of Student's marks
data={
    "Alice": 85,
    "Bob": 45,
    "Charlie": 59,
    "Logan":87
}
name=input("Enter the student's name: ")
if name in data:
    print(f"{name}'s marks: {data[name]}")
else:
    print("Student not found.")

WORKING

We created a dictionary named data in which student names are keys and their marks are their values.

After we take input from the user dynamically using input() function of the student's name and by checking if the student name is in the dictionary, if the name matches, the we print their corresponding marks, if no found we print that Student not found.

EXAMPLE

if the studend is Alice, then the output will be:

Alice's marks: 85

Task 2: Demonstrate List Slicing 

CODE

#Demonstrating List Slicing
nums=[1,2,3,4,5,6,7,8,9,10]
print("Original list: ",nums)
extracted=nums[0:5]
print("Extracted first five elements: ",extracted)
print("Reversed extracted elements: ",extracted[::-1])

WORKING

Created a list named nums of integers from 1 to 10 and the printed 1st line of the original list , then we created another list named extracted and gave values by slicing from starting index to 5th as the stop part in the slicing is always excluded.

Then we printed the extracted list and then we printed its reversed form by using slicing only by not giving any values for both start and stop fields , but giving the step size as -1 to travel in backward direction.

EXAMPLE

The output will be:

Original list:  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Extracted first five elements:  [1, 2, 3, 4, 5]

Reversed extracted elements:  [5, 4, 3, 2, 1]
