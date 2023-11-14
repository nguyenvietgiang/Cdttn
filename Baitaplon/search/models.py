from django.db import models

# Định nghĩa một lớp WordEntry để lưu trữ thông tin về từ vựng
class WordEntry:
    def __init__(self, vietnamese_meaning, image_url, pronunciation):
        self.vietnamese_meaning = vietnamese_meaning
        self.image_url = image_url
        self.pronunciation = pronunciation

# Định nghĩa lớp HashTable để lưu trữ các đối tượng WordEntry
class HashTable:
    def __init__(self, size):
        # Khởi tạo HashTable với một kích thước cố định và một mảng chứa giá trị None
        self.size = size
        self.table = [None] * size

    # Hàm băm để xác định chỉ mục trong HashTable
    def _hash_function(self, key):
        # băm key thành index sử dụng giá trị hash của key và sau đó chia lấy dư cho kích thước của HashTable (self.size).
        hash_value = hash(key) % self.size
        return hash_value

    # Hàm chèn một khóa và giá trị tương ứng vào HashTable
    def insert(self, key, word_entry):
        #sử dụng hash để băm khi thêm dữ liệu vào
        index = self._hash_function(key)
        # Nếu ô trong HashTable chưa có giá trị, khởi tạo nó là một danh sách rỗng
        if self.table[index] is None:
            self.table[index] = []
        # Thêm tuple (khóa, giá trị) vào danh sách tại chỉ mục đã tính toán
        self.table[index].append((key, word_entry))

    # Hàm tìm kiếm giá trị theo khóa trong HashTable
    def search(self, key):
        index = self._hash_function(key)
        # Kiểm tra xem ô trong HashTable có giá trị hay không
        if self.table[index] is not None:
            # Duyệt qua danh sách tại chỉ mục đã tính toán
            for stored_key, word_entry in self.table[index]:
                # Nếu khóa trùng khớp, trả về giá trị tương ứng
                if stored_key == key:
                    return word_entry
        # Trả về None nếu không tìm thấy giá trị cho khóa đã cho
        return None
