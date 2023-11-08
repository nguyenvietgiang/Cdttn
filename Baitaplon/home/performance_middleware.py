import time
from datetime import datetime

class PerformanceMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()
        response = self.get_response(request)
        end_time = time.time()
        processing_time = end_time - start_time
        response_size = len(response.content)
        formatted_start_time = datetime.fromtimestamp(start_time).strftime('%Y-%m-%d %H:%M:%S')

        # Ghi thông tin vào file log với start_time
        with open('app.log', 'a') as log_file:
            log_file.write(f'[INFO] {formatted_start_time} - {request.method} {request.path} - Processed in {processing_time:.2f} seconds, Response size: {response_size} bytes\n')

        return response
