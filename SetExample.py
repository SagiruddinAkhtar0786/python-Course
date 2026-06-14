s ={3,5,3,2,2,6,"fsagit","sagir",True,False,3.14   }
print(s,end=" ")
print("\nLength of set:", len(s))
print(type(s))  

typeof = set() # empty set
print(type(typeof))
dict1 = {} #this is not a set, this is a dictionary
print(type(dict1))
print("****************************************** \n")
k1 = {1,2,3,4,5}
k2 = {4,5,6,7,8}
print(k1,k2)
print("Union of k1 and k2:", k1 | k2)  # Output: {1, 2, 3, 4, 5, 6, 7, 8}
print("Intersection of k1 and k2:", k1 & k2)  # Output: {4, 5}
print("Difference of k1 and k2:", k1 - k2)  # Output: {1, 2, 3}
print("Symmetric Difference of k1 and k2:", k1 ^ k2)  # Output: {1, 2, 3, 6, 7, 8}  
print("Is k1 a subset of k2?", k1.issubset(k2))  # Output: False
print("Is k1 a superset of k2?", k1.issuperset(k2))  # Output: False
print("Are k1 and k2 disjoint?", k1.isdisjoint(k2))  # Output: False    

print("******************************************")
p1={"sagir","rahul","akhtar","python"}
p2={"python","java","c++","sagir"}
print("Union of p1 and p2:", p1.union(p2))  # Output: {'sagir', 'rahul', 'akhtar', 'python', 'java', 'c++'}
print("Intersection of p1 and p2:", p1.intersection(p2))  # Output: {'sagir', 'python'}
print("Difference of p1 and p2:", p1.difference(p2))  # Output: {'rahul', 'akhtar'}
print("Symmetric Difference of p1 and p2:", p1.symmetric_difference(p2))  # Output: {'rahul', 'akhtar', 'java', 'c++'}  
print("Is p1 a subset of p2?", p1.issubset(p2))  # Output: False
print("Is p1 a superset of p2?", p1.issuperset(p2))  # Output: False
print("Are p1 and p2 disjoint?", p1.isdisjoint(p2))  # Output: False