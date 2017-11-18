class Item(object):

    def __init__(self,key,value):

        self.key = key
        self.value = value

class HashTable(object):

    def __init__(self,size):

        self.size = size
        self.table = [[] for _ in range(self.size)]


    def hash(self,key):
        return key % self.size

    def set (self,key,value):
        hash_index = self.hash(key)
        for item in self.table[hash_index]:
            if item.key == key:
                item.value = value
                return
        self.table[hash_index].append(Item(key,value))

    def get(self, key):
        hash_index = self.hash(key)
        for item in self.table[hash_index]:
            if item.key == key:
                return item.value
        raise Exception("no such key")


    def remove(self,key):
        hash_index = self.hash(key)
        for index,item in enumerate(self.table[hash_index]):
            del self.table[hash_index][index]
            return print("removed",key)
        raise Exception("no such key")


def main():
    test = HashTable(10)

    test.set(10,2)
    print(test.get(10))
    test.set(10,2000)
    print(test.get(10))
    test.remove(10)

if __name__ == '__main__':
    main()


