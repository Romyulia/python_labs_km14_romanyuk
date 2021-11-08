salary_list = [7.3, 8.5, 11, 12.7, 15.2, 21.12, 27.35]
print("Salary table:")
new_salary_list = list(map(lambda i: round(i + i * 0.3, 2), salary_list))
indexing = list(map(lambda i: round(i * 0.3, 2), salary_list))
for i in range(len(salary_list)):
    print(salary_list[i], new_salary_list[i], indexing[i])