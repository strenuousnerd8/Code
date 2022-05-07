class HashTable:
    def __init__(self, size = 7):
        self.data_map = [None] * size

    def __hash(self, key):
        my_hash = 0
        for letter in key:
            index = my_hash + (ord(letter) * 23) % len(self.data_map)
        return index

    def print_all(self):
        for i, val in enumerate(self.data_map):
            print(str(i) + " :", val)

    def sethash(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    def gethash(self, key):
        index = self.__hash(key)
        similar = []
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    similar.append(self.data_map[index][i][1])
            return similar
        return None

    def keys(self):
        all_keys = []
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][j][0])
        return all_keys

new_hash = HashTable()
new_hash.sethash('Faiz', 1200)
new_hash.sethash('Aftab', 786)
new_hash.sethash('Azeem', 9899)
new_hash.sethash('Aftab', 3228)
new_hash.print_all()
print(new_hash.gethash('Aftab'))
print(new_hash.keys())