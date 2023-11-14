import time
from datetime import datetime
import psutil

class PerformanceMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.perf_counter()
        response = self.get_response(request)
        end_time = time.perf_counter()
        processing_time = end_time - start_time
        response_size = len(response.content)
        formatted_start_time = datetime.fromtimestamp(start_time).strftime('%Y-%m-%d %H:%M:%S')

        # Ghi thông tin vào file log với start_time, CPU, và bộ nhớ
        cpu_usage = psutil.cpu_percent()
        memory_usage = psutil.virtual_memory().percent

        with open('app.log', 'a') as log_file:
            log_file.write(f'[INFO] {formatted_start_time} - {request.method} {request.path} - Processed in {processing_time:.6f} seconds, Response size: {response_size} bytes, CPU Usage: {cpu_usage}%, Memory Usage: {memory_usage}%\n')

        return response

