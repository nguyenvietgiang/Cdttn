from django.shortcuts import render

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

def get_product(request):
    hash_table = HashTable(1000)
    hash_table.insert("Hello", WordEntry("xin chào", "https://media.makeameme.org/created/hello-sir-my-59f1d3.jpg", "https://dictionary.cambridge.org/vi/media/english/uk_pron/u/ukh/ukhef/ukheft_029.mp3"))
    hash_table.insert("Football", WordEntry("Bóng đá", "https://images.indianexpress.com/2022/06/india-Football-pic-credit-aiff.jpg", "https://dictionary.cambridge.org/media/english/us_pron/f/foo/footb/football.mp3"))
    hash_table.insert("Movie", WordEntry("Phim điện ảnh", "https://cdn.marvel.com/content/1x/antmanandthewaspquantumania_lob_crd_03.jpg", "https://dictionary.cambridge.org/media/english/uk_pron_ogg/u/ukm/ukmou/ukmourn022.ogg"))
    hash_table.insert("Dog", WordEntry("Con chó", "https://dictionary.cambridge.org/images/thumb/dog_noun_001_04904.jpg", "https://dictionary.cambridge.org/media/english/us_pron_ogg/d/dog/dog__/dog.ogg"))
    hash_table.insert("Run", WordEntry("Chạy đi", "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a8/Flickr_cc_runner_wisconsin_u.jpg/220px-Flickr_cc_runner_wisconsin_u.jpg", "https://dictionary.cambridge.org/vi/media/english/uk_pron/u/ukr/ukrum/ukrum__018.mp3"))
    english_word = None
    word_entry = None

    if request.method == 'POST':
        english_word = request.POST.get('english_word')
        if english_word:
            word_entry = hash_table.search(english_word)

    return render(request, 'search.html', {'english_word': english_word, 'word_entry': word_entry})


