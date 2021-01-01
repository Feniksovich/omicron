summ = 0

# 0 не является ни положительным, ни отрицательным числом
for i in range(1, 100): 
    if i%7 == 0:
        summ += i
print(summ)