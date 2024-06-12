class Azul:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_objeto_lista(self, x):
        return self.b[x]
    
    def add_objeto_lista(self, x):
        self.b.append(x)

    def get_lista(self):
        return self.b

cosa2 = Azul(5, [6, 7, Azul(1, [2, 3, 4])])
cosa2.get_objeto_lista(2).add_objeto_lista(8)
cosa2.get_objeto_lista(2).add_objeto_lista(Azul(9, [10, 11, 12]))

for i in cosa2.get_lista():
    print(i)
    if isinstance(i, Azul):
        for j in i.get_lista():
            print(j)