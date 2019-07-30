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









# class Hashtable:
#     def __init__(self):
#         self.size = 5
#         self.map = [[] for _ in range(4//2)]
#
#
#
#
#     def hash_func(self, key): #assuming our KEY is a string.
#         hash = 0
#         for char in str(key): #string cast then do ord checking.
#             hash += ord(char) #gives ascii value.
#
#         return hash % self.size    #another simple way for hash function is to key % len(self.size)
#
#
#
#
#     # def contains(self, key):
#     #     hash_key = self.hash_func(key)
#     #     if hash_key in self.map[hash_key][0]:
#     #         return True
#     #     else:
#     #         return False
#     def set(self, key , value): #basically adding key values. #ADD FUNCTION / SET FUNCTION BASICALLY.
#         # key_hash = self.hash_func(key) #hashed key.
#         # key_value = (key, value) #key value pair.
#         #
#         # if self.map[key_hash]:
#         #     self.map[key_hash] = list
#         # for pair in self.map[key_hash]:
#         #
#         key_hash = self.hash_func(key) #idx value we place in or slot
#         bucket = self.map[key_hash]
#         key_exists = False
#
#         for idx ,keyval in enumerate(bucket):
#             cur_key, cur_value = keyval
#
#             if cur_key == key:
#                 key_exists = True
#                 break
#         if key_exists:
#             bucket[idx] = ((key,value ))
#         else:
#             bucket.append((key,value ))



        # if self.map[key_hash] is None: # you can just add the key value inside.
        #     self.map[key_hash] = list([key_value])
        #     return True
        # else:
        #     for pair in self.map[key_hash]: #check if key exists then.
        #         if pair[0] == key:
        #             pair[1] = value
        #             return True
        #     self.map[key_hash].append(key_value) #else it's a new key then we just add it like so
        #     return True
    #
    # def get(self, key):
    #     key_hash = self.hash_func(key)
    #     if self.map[key_hash] is not None:
    #         for pair in self.map[key_hash]:
    #             if pair[0] == key:
    #                 return pair[1]
    #     return None
    #
    # def delete(self,key):
    #     key_hash = self.hash_func(key)
    #
    #     if self.map[key_hash] is None:
    #         return False
    #     for idx in range(0, len(self.map[key_hash])):
    #         if self.map[key_hash][idx][0] == key:
    #             self.map[key_hash].pop(idx)
    #             return True
    #
    #
    # def print(self):
    #     print(' ---- INFO ----')
    #     for item in self.map:
    #         if item is not None:
    #             print(str(item))


ans = Hashtable(5)
ans.set('Bob', '415-504-6510')
ans.set('Ming', '428-348-3912')
ans.set('Luler' ,'123')
ans.set('Otherman', '456')
ans.delete('Otherman')
ans.print()

