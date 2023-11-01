from django.shortcuts import render
# sử dụng để thực hiện các truy vấn and, or
from django.db.models import Q
from .models import DictionaryEntry, Conversation
from django.http import JsonResponse


# Tải dữ liệu từ cơ sở dữ liệu và chuyển đổi thành một từ điển (dictionary)
# Các từ tiếng Anh là khóa (key), và các dịch tiếng Việt tương ứng là giá trị (value)
def load_data_into_dictionary():
    # Lấy tất cả các bản ghi từ model DictionaryEntry
    translation_records = DictionaryEntry.objects.all()
    english_to_vietnamese = {}

    # Duyệt qua các bản ghi và thêm chúng vào từ điển
    for record in translation_records:
        english_to_vietnamese[record.english] = record.vietnam

    # Trả về từ điển với dữ liệu đã được tải
    return english_to_vietnamese

# Gọi hàm để tải dữ liệu từ cơ sở dữ liệu vào biến english_to_vietnamese
english_to_vietnamese = load_data_into_dictionary()

# Hàm xử lý yêu cầu dịch từ tiếng Anh sang tiếng Việt
def translate(request):
    # Kiểm tra xem yêu cầu được gửi dưới dạng phương thức GET hay không
    if request.method == 'GET':
        # Lấy từ tiếng Anh từ tham số truy vấn 'english_word' trong URL
        english = request.GET.get('english_word', '')
        
        # Tìm kiếm từ tiếng Anh trong từ điển đã tải
        # Nếu không tìm thấy, trả về thông báo "Không tìm thấy từ tương ứng."
        vietnamese_translation = english_to_vietnamese.get(english, "Không tìm thấy từ tương ứng.")
        
        # Trả về trang web với kết quả dịch tiếng Việt và từ tiếng Anh được tìm kiếm
        return render(request, 'translate.html', {'vietnamese_translation': vietnamese_translation, 'english_word': english})

    # Nếu yêu cầu không phải là GET, trả về trang web mặc định cho việc dịch từ tiếng Anh sang tiếng Việt
    return render(request, 'translate.html')

# Khởi tạo một dict để lưu trữ kết quả cache
search_cache = {}

def search(request):
    search_query = request.GET.get('search_query')

    if search_query:
        # Kiểm tra xem có kết quả tìm kiếm trong cache hay không
        results = search_cache.get(search_query)

        if results is None:
            dictionary_results = DictionaryEntry.objects.filter(english__icontains=search_query)
            conversation_results = Conversation.objects.filter(enconversation__icontains=search_query)

            # Tạo danh sách kết quả
            results = []
            for dictionary_entry in dictionary_results:
                results.append(('dictionary', dictionary_entry))
            for conversation_entry in conversation_results:
                results.append(('conversation', conversation_entry))
            # Lưu kết quả vào cache
            search_cache[search_query] = results
            # Ghi thông tin vào log trong terminal
        print("Results:", results)

        return render(request, 'search_results.html', {'results': results, 'search_query': search_query})
    else:
        return render(request, 'home.html')

def search_suggestions(request):
    search_query = request.GET.get('search_query', '')
    suggestions = DictionaryEntry.objects.filter(english__icontains=search_query)[:5]
    suggestion_list = [entry.english for entry in suggestions]
    return JsonResponse(suggestion_list, safe=False)


def get_home(request):
    return render(request,'home.html') 
