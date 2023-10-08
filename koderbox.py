a = {"a":0,"b":1,"c":2}
b = {"az":0,"bz":1,"cz":2}

##  op = {"az":{"a":0},"bz":{"b":1},"cz":{"c":2}}

op = {}
for b_key,b_value in b.items():
    op[b_key] = {}
    for a_key, a_value in a.items():
        op[b_key]={a_key:[a_value]}

print(op)


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9
fahrenheit_temperatures = [32, 68, 86, 104, 122]
list1 = []
# for i in fahrenheit_temperatures:
#     value = fahrenheit_to_celsius(i)
#     list1.append(value)
# print(list1)

list1 = list(map(fahrenheit_to_celsius,fahrenheit_temperatures))
print(list1)


ages = [16, 22, 18, 25, 15, 30, 17, 20]

# Function to check if an age is eligible for voting
def is_eligible_for_voting(age):
    if age >= 18:
        return age
elig_age_list=[]
elig_age_list = list(filter(is_eligible_for_voting,ages))
print(elig_age_list)
elig_age_list = list(map(is_eligible_for_voting,ages))
print(elig_age_list)

#  where we have two lists of data: one containing names of students and another 
# containing their corresponding exam scores. We want to create a dictionary 
# that maps the names of students to their scores but only include students who
# scored above a certain threshold. We will use map(), filter(), zip(),
#  and dictionary comprehension to achieve this.
 
# 1st approach
student_names = ["Alice", "Bob", "Charlie", "David", "Eve"]
exam_scores = [85, 92, 78, 65, 90]
threshold_score = 80
# output  =  {'Alice': 85, 'Bob': 92, 'Eve': 90} 
student = zip(student_names,exam_scores)
# for i in student:
#     print(i[0])
#     print(i[1])
filterdata =filter(lambda i:i[1] > threshold_score , student)

student_scores = {name : score for name,score in filterdata}
print(student_scores)


#2nd approach using a function
student_names = ["Alice", "Bob", "Charlie", "David", "Eve"]
exam_scores = [85, 92, 78, 65, 90]
threshold_score = 80

student_data = zip(student_names,exam_scores)

def filter_stud(student_data):
    Name ,score = student_data
    return score>threshold_score
filterdata = filter(filter_stud,student_data)
print(dict(filterdata))

### board size 10*10

# def board_size(range_num):
   
# #     print(range_num)
#     board_data = {
#         'Square': list(range(1,range_num+1))
#     }
# #     print(board_data)
#     board = pd.DataFrame(board_data)
#     print(board)
#     return board

### random_dice

# def roll_dice():
#     return(random.randint(1,6))

### playgame = 4 player jo sbse phle 100 par karega  use jitha dena h