marks= [30,54,64,78,9078,90,85,72,60,45,80]


#for mark in marks:    print(mark)

for index, mark in enumerate(marks):
    print(index, mark)

print(marks , end=" ")
marks.append(95)
print(marks)
marks.insert(2, 88)
print(marks)    
marks.remove(64)
print(marks)    
marks.sort()
print(marks)
marks.reverse()
print(marks)
print("Length of marks list:", len(marks))
print("Maximum mark:", max(marks))
print("Minimum mark:", min(marks))
print("Average mark:", sum(marks) / len(marks))
print("Number of marks above 80:", len([mark for mark in marks if mark > 80]))
print("Marks between 50 and 80:", [mark for mark in marks if 50 <= mark <= 80])
print("Marks in descending order:", sorted(marks, reverse=True))
print("Marks in ascending order:", sorted(marks))
print("Marks as a set (unique values):", set(marks))
print("Marks as a tuple:", tuple(marks))
print(marks.count(30), "students scored 30")
marks2 = [23,21,32]
joined_marks = marks + marks2
print("Joined marks:", joined_marks)

marks.extend(marks2)
print("Extended marks:", marks)