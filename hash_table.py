import sys


class HashTable:
    def __init__(self, table_size):
        if table_size < 1:
            print("Erro: o tamanho da tabela tem que ser positivo")
            sys.exit(1)
        
        self.table_size = table_size
        self.table = [[] for i in range(self.table_size)]

    def hash_func(self, key):
        return key % self.table_size
    
    def insert(self, key):
        self.table[self.hash_func(key)].append(key)

    def show(self):
        for linked_list in self.table:
            if linked_list:
                for key in linked_list:
                    print("%d" % key, end=" ")
                print(" ")
    
    def search(self):
        return key in self.table[self.hash_func(key)]


d = HashTable(9)
d.insert(19) 
d.insert(28) 
d.insert(20) 
d.insert(5) 
d.insert(33) 
d.insert(15)

d.show() 