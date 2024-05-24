
class Fibonacci:
    def __init__(self):
        self.a = 0
        self.b = 1
    def __iter__(self):
        return self
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        return self.a
obj = Fibonacci()
#print(next(obj))
#print(next(obj))
#print(next(obj))
#print(next(obj))
# infinitiy qildik iterator orqali
#tepadagi biz nechta next orqali print qilsak shunch fibonachi sonini chiqaradi
for i in obj:
    print(i)
#bu orqali cheksiz davom etadi fibonachi sonlari yani infinity

