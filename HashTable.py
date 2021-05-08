class HashEntry: #SEPERATE CHAINING.
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None #ll.next

    def print(self):
        print("  '" + self.key + "' / " + str(self.value))

class Hashtable:
    def __init__(self, size):
        self.size = size #size of list
        self.table = [[] for _ in range(10) ]

    def hashing_function(self, key):
        hash = 0
        for char in str(key): #string cast then do ord checking.
            hash += ord(char) #gives ascii value.

        return hash % self.size    #another simple way for hash function is to key % len(self.size)

    def rehash(self, entry, key, value):
        while entry and entry.key != key:
            prev, entry = entry, entry.next
        if entry:
            entry.value = value
        else:
            prev.next = HashEntry(key, value)

    def set(self, key, value): #setter
        slot = self.hashing_function(key) #open slot slot?
        entry = self.table[slot] # get the entry from the slot.
        if not entry:
            self.table[slot] = HashEntry(key, value)
        else:
            self.rehash(entry, key, value)

    def get(self, key): #gette
        hash = self.hashing_function(key)
        if not self.table[hash]:
            raise KeyError
        else:
            entry = self.table[hash]
            while entry and entry.key != key: entry = entry.next
            return entry.value

    def print(self):
        print(' ---- INFO ----')
        dummy_list = []
        for item in self.table:
            if item == dummy_list:
                continue
            if item.key and item.value:
                print(item.key, item.value)
            if item.next:
                item = item.next
                print(item.key, item.value)
            else:
                continue

    def delete(self, key):
        slot = self.hashing_function(key)
        entry = self.table[slot]
        while entry is not None:
            if entry.key == key:
                break
            prev = entry
            entry = entry.next

        prev.next = entry.next


ans = Hashtable(5)
ans.set('Bob', '415-504-6510')
ans.set('Ming', '428-348-3912')
ans.set('Luler' ,'123')
ans.set('Otherman', '456')
ans.delete('Otherman')
ans.print()

