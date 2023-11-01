from django.shortcuts import render,redirect
from home.models import DictionaryEntry
from .forms import EnglishInputForm
from random import choice

def test_view(request):
    # Kiểm tra xem random_entry_id đã được lưu trong session chưa
    if 'random_entry_id' not in request.session:
        # Nếu chưa có, chọn một random_entry_id mới
        random_entry_id = choice(DictionaryEntry.objects.values_list('id', flat=True))
        # Lưu random_entry_id vào session
        request.session['random_entry_id'] = random_entry_id
    else:
        # Nếu đã có, lấy random_entry_id từ session
        random_entry_id = request.session['random_entry_id']

    # Lấy bản ghi từ random_entry_id
    random_entry = DictionaryEntry.objects.get(id=random_entry_id)

    feedback = None

    if request.method == 'POST':
        form = EnglishInputForm(request.POST)
        if form.is_valid():
            english_input = form.cleaned_data['english_input']
            if english_input == random_entry.english:
                feedback = 'Chính xác!'
            else:
                feedback = 'Không chính xác! Hãy thử lại.'
    else:
        form = EnglishInputForm()

    context = {
        'random_entry': random_entry,
        'form': form,
        'feedback': feedback,
    }
    return render(request, 'test.html', context)

def change_word_view(request):
    used_entry_ids = request.session.get('used_entry_ids', [])
    available_entry_ids = set(DictionaryEntry.objects.values_list('id', flat=True)) - set(used_entry_ids)

    if available_entry_ids:
        random_entry_id = choice(list(available_entry_ids))
        request.session['random_entry_id'] = random_entry_id
        used_entry_ids.append(random_entry_id)
        request.session['used_entry_ids'] = used_entry_ids

    # Chuyển hướng người dùng trở lại trang test_view sau khi đổi từ
    return redirect('test_view')
