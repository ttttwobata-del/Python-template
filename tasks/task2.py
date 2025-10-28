# tasks/task2.py

def solve():
# Ниже пишите решение задачи
    n = input()
    a = int(n[0]) + int(n[1]) + int(n[2])
    b = 0
    for i in range(3, len(n)):
    b += int(n[i])
    print(a, b)
   

   
# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()
