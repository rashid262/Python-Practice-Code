# NestedList

# n = int(input())
# main_list = []
# for i in range(n):
#     name = input()
#     score = float(input())
#     main_list.append([name, score])
# 
# marks = []
# for name,score in main_list:
#     marks.append(score)
# 
# set1 = set(marks)
# final_score = list(set1)
# final_score = final_score.sort()
# print(final_score[1])

n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
specific_student_marks = student_marks[query_name]
sum = 0
for i in specific_student_marks:
    sum += i

print(float(sum/len(specific_student_marks)))





