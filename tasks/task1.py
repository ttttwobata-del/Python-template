# tasks/task1.py

def solve():
# Ниже пишите решение задачи
    n = int(input())
    print(n // 100 + n // 10 % 10 + n % 10)


# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()
