from django.db import models

class WordEntry:
    def __init__(self, vietnamese_meaning, image_url, pronunciation):
        self.vietnamese_meaning = vietnamese_meaning
        self.image_url = image_url
        self.pronunciation = pronunciation

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def _hash_function(self, key):
        hash_value = hash(key) % self.size
        return hash_value

    def insert(self, key, word_entry):
        index = self._hash_function(key)
        if self.table[index] is None:
            self.table[index] = []
        self.table[index].append((key, word_entry))

    def search(self, key):
        index = self._hash_function(key)
        if self.table[index] is not None:
            for stored_key, word_entry in self.table[index]:
                if stored_key == key:
                    return word_entry
        return None