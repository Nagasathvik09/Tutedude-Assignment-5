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
