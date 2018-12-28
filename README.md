## CuckooHash
The CuckooHash class implements 5 methods (including the constructor):
* constructor(size): return an instance of the class with pre-allocated space for the given number of objects.
* boolean set(key, value): stores the given key/value pair in the hash map. Returns a boolean value indicating success / failure of the operation.
* get(key): return the value associated with the given key, or null if no value is set.
* delete(key): delete the value associated with the given key, returning the value on success or null if the key has no value.
* float load(): return a float value representing the load factor (`(items in hash map)/(size of hash map)`) of the data structure. Since the size of the dat structure is fixed, this should never be greater than 1.

## Implementation
This specific implementation follows that of the original paper (Pugh and Rodler, 2001) except that:
* only a single table was used, as opposed to one for each hash function, in order to keep the code as simple as possible
* 8 hash functions were used instead of 2 to improve performance at higher load factors. This meant that when a new key/value pair was being set, first all 8 hashes were computed and the pair was placed in the first slot that was free. If all of the hashes led to collisions, the pair was placed in the slot corresponding to the first hash, and the process was repeated for the pair that was bumped out of the table.