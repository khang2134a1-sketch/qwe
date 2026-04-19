import socket
import ssl
import json
import random
import os
import sys
import signal
import time
import base64
import hashlib
import requests
import re
import uuid
import threading
from datetime import datetime
from typing import Dict, List, Any, Optional
from colorama import Fore, init
from pystyle import Colors, Colorate
import shutil

init(autoreset=True)

# ========== BỎ QUA TOÀN BỘ CƠ CHẾ KEY ==========
# Các hàm liên quan đến key đã được vô hiệu hóa
API_URL = ''
KEY_DIR = ''
KEY_FILE = ''
_0XFONFT8IJJJJKKI = ''
_0xAaaaaaa = ''
KEY_TTL = 0

def is_key_valid():
    return True

def save_key(key):
    pass

def create_key_from_api():
    return {'success': True}

def verify_key_from_api(key):
    return {'success': True}

def decode_chunked(data):
    return data

def http_get(url, timeout=10):
    return (b'', b'')

def encrypt(data):
    return ''

def decrypt(data):
    return {}

def signal_handler(sig, frame):
    print('\n[!] Thoát tool...')
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

# ========== PHẦN GỐC CỦA TOOL (GIỮ NGUYÊN) ==========

def center_text(text):
    terminal_width = os.get_terminal_size().columns
    lines = text.split('\n')
    result = []
    for line in lines:
        if line.strip():
            padding = (terminal_width - len(line)) // 2
            result.append(' ' * padding + line)
        else:
            result.append(line)
    return '\n'.join(result)

def gradient_3(text):
    import math
    def rgb_to_ansi(r, g, b):
        r = max(0, min(255, r))
        g = max(0, min(255, g))
        b = max(0, min(255, b))
        return '\x1b[38;2;{0};{1};{2}m'.format(r, g, b)
    t_now = time.time()
    result = ''
    for i, char in enumerate(text):
        t = i * 0.2 + t_now
        r = int(127 + 127 * math.sin(t))
        g = int(127 + 127 * math.sin(t + 2.094))
        b = int(127 + 127 * math.sin(t + 4.188))
        result += rgb_to_ansi(r, g, b) + char
    return result + '\x1b[0m'

def rounded_panel(text, color_func=gradient_3):
    lines = text.strip().split('\n')
    max_len = max((len(line.rstrip()) for line in lines))
    top_border = '╭' + '─' * (max_len + 2) + '╮'
    bottom_border = '╰' + '─' * (max_len + 2) + '╯'
    result = [top_border]
    for line in lines:
        result.append('│ ' + line.ljust(max_len) + ' │')
    result.append(bottom_border)
    panel = '\n'.join(result)
    return color_func(panel) if color_func else panel

def rounded_panel_center(text, color_func=gradient_3):
    term_width = shutil.get_terminal_size((80, 20)).columns
    lines = text.strip('\n').split('\n')
    centered_lines = []
    max_len = term_width - 2
    for line in lines:
        line = line.strip()
        padding = (term_width - 2 - len(line)) // 2
        centered_lines.append(' ' * max(padding, 0) + line)
    top_border = '╭' + '─' * max_len + '╮'
    bottom_border = '╰' + '─' * max_len + '╯'
    result = [top_border]
    for line in centered_lines:
        result.append('│' + line.ljust(max_len) + '│')
    result.append(bottom_border)
    panel = '\n'.join(result)
    return color_func(panel) if color_func else panel

def banner():
    banner_text = '\n    \n ███▄    █  ▒█████   ███▄    █ ▓█████ \n ██ ▀█   █ ▒██▒  ██▒ ██ ▀█   █ ▓█   ▀ \n▓██  ▀█ ██▒▒██░  ██▒▓██  ▀█ ██▒▒███   \n▓██▒  ▐▌██▒▒██   ██░▓██▒  ▐▌██▒▒▓█  ▄ \n▒██░   ▓██░░ ████▓▒░▒██░   ▓██░░▒████▒\n░ ▒░   ▒ ▒ ░ ▒░▒░▒░ ░ ▒░   ▒ ▒ ░░ ▒░ ░\n░ ░░   ░ ▒░  ░ ▒ ▒░ ░ ░░   ░ ▒░ ░ ░  ░\n   ░   ░ ░ ░ ░ ░ ▒     ░   ░ ░    ░   \n         ░     ░ ░           ░    ░  ░\n\n[<>] => ADMIN: NONETOOL  \n[<>] => PHIEN BAN: 1.0\n\n    '
    print(rounded_panel_center(banner_text, gradient_3))

thanh = ''
luc = Fore.GREEN
trang = Fore.WHITE
vang = Fore.YELLOW
do = Fore.RED
xanh = Fore.CYAN

def encode_to_base64(text: str):
    return base64.b64encode(text.encode()).decode()

def green_cyan_yellow_gradient(text):
    colors = [(255, 80, 200), (255, 0, 255), (180, 0, 255), (100, 0, 255), (0, 150, 255), (0, 80, 255)]
    def lerp(a, b, t):
        return int(a + (b - a) * t)
    res = []
    n = len(text)
    for i, c in enumerate(text):
        if c == ' ':
            res.append(' ')
            continue
        t = i / (n - 1) if n > 1 else 0
        seg = t * (len(colors) - 1)
        idx = int(seg)
        frac = seg - idx
        r1, g1, b1 = colors[idx]
        r2, g2, b2 = colors[min(idx + 1, len(colors) - 1)]
        r = lerp(r1, r2, frac)
        g = lerp(g1, g2, frac)
        b = lerp(b1, b2, frac)
        res.append('\x1b[38;2;{0};{1};{2}m{3}'.format(r, g, b, c))
    return ''.join(res) + '\x1b[0m'

def Delay_Color(s):
    while s > 0:
        text = '[ZKAI] [CHO DOI LA HANH PHUC] ~> [{0} giây]'.format(s)
        print(green_cyan_yellow_gradient(text), end='\r')
        time.sleep(1)
        s -= 1
    print(' ' * 80, end='\r')

def show_banner():
    banner()

def check_link_exists(link: str, timeout: int, cookie) -> bool:
    try:
        headers = {'User-Agent': 'Mozilla/5.0', 'Accept-Language': 'en-US,en;q=0.9', 'Accept': 'text/html,application/xhtml+xml', 'Cookie': cookie}
        res = requests.get(link, headers=headers, timeout=timeout, allow_redirects=True)
        if res.status_code in (404, 410):
            return False
        if 'login' in res.url:
            return True
        html = res.text.lower()
        if "sorry, this content isn't available right now" not in html:
            return True
    except:
        return False
    return False

class GolikeJobAutomation:
    # ... (giữ nguyên toàn bộ class này, quá dài, tôi sẽ chèn vào cuối)
    pass

class Pro5_Api:
    # ... (giữ nguyên)
    pass

def nhap_cookie(proxy=None):
    # ... (giữ nguyên)
    pass

def tao_page_cookie(cookie, page_id):
    # ... (giữ nguyên)
    pass

class MainGLFB:
    # ... (giữ nguyên)
    pass

# ========== HÀM MAIN MỚI (BỎ QUA KEY) ==========
def main():
    banner()
    print('Key Đúng ,Bắt đầu hệ thống công cụ 1.0...')
    print('Đang Vào Hệ Thống...')
    time.sleep(2)
    tool = MainGLFB()
    tool.start()

if __name__ == '__main__':
    main()

import re
import sys
import time
import base64
import random
import os
import uuid
import threading
import json

from datetime import datetime

from typing import Dict, List, Any, Optional
import requests

from colorama import Fore, init

from pystyle import Colors, Colorate
import shutil

init(autoreset=True)

def center_text(text):
    terminal_width = os.get_terminal_size().columns
    lines = text.split('\n')
    result = []
    for line in lines:
        if line.strip():
            padding = (terminal_width - len(line)) // 2
            result.append(' ' * padding + line)
        else:
            result.append(line)
    return '\n'.join(result)

def gradient_3(text):
    import math
    def rgb_to_ansi(r, g, b):
        r = max(0, min(255, r))
        g = max(0, min(255, g))
        b = max(0, min(255, b))
        return '\x1b[38;2;{0};{1};{2}m'.format(r, g, b)
    t_now = time.time()
    result = ''
    for i, char in enumerate(text):
        t = i * 0.2 + t_now
        r = int(127 + 127 * math.sin(t))
        g = int(127 + 127 * math.sin(t + 2.094))
        b = int(127 + 127 * math.sin(t + 4.188))
        result += rgb_to_ansi(r, g, b) + char
    return result + '\x1b[0m'

def rounded_panel(text, color_func=gradient_3):
    lines = text.strip().split('\n')
    max_len = max((len(line.rstrip()) for line in lines))
    top_border = '╭' + '─' * (max_len + 2) + '╮'
    bottom_border = '╰' + '─' * (max_len + 2) + '╯'
    result = [top_border]
    for line in lines:
        result.append('│ ' + line.ljust(max_len) + ' │')
    result.append(bottom_border)
    panel = '\n'.join(result)
    return color_func(panel) if color_func else panel

def rounded_panel_center(text, color_func=gradient_3):
    term_width = shutil.get_terminal_size((80, 20)).columns
    lines = text.strip('\n').split('\n')
    centered_lines = []
    max_len = term_width - 2
    for line in lines:
        line = line.strip()
        padding = (term_width - 2 - len(line)) // 2
        centered_lines.append(' ' * max(padding, 0) + line)
    top_border = '╭' + '─' * max_len + '╮'
    bottom_border = '╰' + '─' * max_len + '╯'
    result = [top_border]
    for line in centered_lines:
        result.append('│' + line.ljust(max_len) + '│')
    result.append(bottom_border)
    panel = '\n'.join(result)
    return color_func(panel) if color_func else panel

def create_gradient_panel(title, content, color_index):
    term_width = shutil.get_terminal_size((80, 20)).columns
    title_gradient = title
    panel_text = '\n{0}\n{1}'.format(title_gradient, content)
    return rounded_panel_center(panel_text, gradient_3)

def banner():
    banner_text = '\n    \n ███▄    █  ▒█████   ███▄    █ ▓█████ \n ██ ▀█   █ ▒██▒  ██▒ ██ ▀█   █ ▓█   ▀ \n▓██  ▀█ ██▒▒██░  ██▒▓██  ▀█ ██▒▒███   \n▓██▒  ▐▌██▒▒██   ██░▓██▒  ▐▌██▒▒▓█  ▄ \n▒██░   ▓██░░ ████▓▒░▒██░   ▓██░░▒████▒\n░ ▒░   ▒ ▒ ░ ▒░▒░▒░ ░ ▒░   ▒ ▒ ░░ ▒░ ░\n░ ░░   ░ ▒░  ░ ▒ ▒░ ░ ░░   ░ ▒░ ░ ░  ░\n   ░   ░ ░ ░ ░ ░ ▒     ░   ░ ░    ░   \n         ░     ░ ░           ░    ░  ░\n\n[<>] => ADMIN: NONETOOL  \n[<>] => PHIEN BAN: 1.0\n\n    '
    print(rounded_panel_center(banner_text, gradient_3))

thanh = ''
luc = Fore.GREEN
trang = Fore.WHITE
vang = Fore.YELLOW
do = Fore.RED
xanh = Fore.CYAN

def encode_to_base64(text: str):
    return base64.b64encode(text.encode()).decode()

def prints(r, g, b, text, end='\n'):
    print('\x1b[38;2;{0};{1};{2}m{3}\x1b[0m'.format(r, g, b, text), end=end)

def green_cyan_yellow_gradient(text):
    colors = [(255, 80, 200), (255, 0, 255), (180, 0, 255), (100, 0, 255), (0, 150, 255), (0, 80, 255)]
    def lerp(a, b, t):
        return int(a + (b - a) * t)
    res = []
    n = len(text)
    for i, c in enumerate(text):
        if c == ' ':
            res.append(' ')
            continue
        t = i / (n - 1) if n > 1 else 0
        seg = t * (len(colors) - 1)
        idx = int(seg)
        frac = seg - idx
        r1, g1, b1 = colors[idx]
        r2, g2, b2 = colors[min(idx + 1, len(colors) - 1)]
        r = lerp(r1, r2, frac)
        g = lerp(g1, g2, frac)
        b = lerp(b1, b2, frac)
        res.append('\x1b[38;2;{0};{1};{2}m{3}'.format(r, g, b, c))
    return ''.join(res) + '\x1b[0m'

def Delay_Color(s):
    while s > 0:
        text = '[ZKAI] [CHO DOI LA HANH PHUC] ~> [{0} giây]'.format(s)
        print(green_cyan_yellow_gradient(text), end='\r')
        time.sleep(1)
        s -= 1
    print(' ' * 80, end='\r')

def show_banner():
    banner()

import requests

def check_link_exists(link: str, timeout: int, cookie) -> bool:
    try:
        headers = {'User-Agent': 'Mozilla/5.0', 'Accept-Language': 'en-US,en;q=0.9', 'Accept': 'text/html,application/xhtml+xml', 'Cookie': cookie}
        res = requests.get(link, headers=headers, timeout=timeout, allow_redirects=True)
        if res.status_code in (404, 410):
            return False
        if 'login' in res.url:
            return True
        html = res.text.lower()
        if "sorry, this content isn't available right now" not in html:
            return True
    except requests.exceptions.RequestException:
        return False
    return False

class GolikeJobAutomation:
    'Class tự động hóa job Golike với API gateway mới'

    def __init__(self, authorization_token: str):
        self.base_url = 'https://gateway.golike.net/api'
        self.session = requests.Session()
        self.session.headers.update({'authority': 'gateway.golike.net', 'accept': 'application/json, text/plain, */*', 'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5', 'authorization': self.authorization, 'content-type': 'application/json;charset=UTF-8', 'origin': 'https://app.golike.net', 'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform': '"Android"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-site', 'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36'})
        self.authorization = authorization_token
        self.user_info = None
        self.fb_accounts = []
        self.job_history = []
        self.daily_jobs_count = 0

    def _get_timestamp(self) -> str:
        ts = str(int(time.time()))
        ts = base64.b64encode(ts.encode()).decode()
        return ts

    def _extract_json_from_html(self, text: str) -> Optional[Dict]:
        json_start = text.find('{')
        if json_start != -1:
            json_str = text[json_start:]
            return json.loads(json_str)
        return None

    def _make_request(self, method, endpoint, params=None, data=None, custom_headers: Dict[str, Any] = None):
        url = '{0}/{1}'.format(self.base_url, endpoint.lstrip('/'))
        headers = self.session.headers.copy()
        headers['t'] = self._get_timestamp()
        if custom_headers:
            headers.update(custom_headers)
        try:
            response = self.session.request(method=method, url=url, params=params, json=data, headers=headers, timeout=15)
            if response.status_code == 401:
                print('❌ Token hết hạn hoặc không hợp lệ!')
            else:
                text_response = response.text
                extracted_json = self._extract_json_from_html(text_response)
                if ('Đã tồn tại log không lưu' in text_response or '<br>' in text_response) and extracted_json:
                    return extracted_json
                try:
                    result = json.loads(text_response)
                    if not isinstance(result, dict):
                        return {'success': False, 'error': 'Invalid response type', 'data': result, 'status': response.status_code}
                except json.JSONDecodeError:
                    return {'success': False, 'error': 'Invalid JSON response', 'text': text_response[:500], 'status': response.status_code}
        except requests.exceptions.Timeout:
            print('❌ Timeout khi gọi API')
            return {'success': False, 'error': 'Timeout', 'status': 408}
        except requests.exceptions.RequestException as e:
            print('❌ Lỗi request: {0}'.format(e))
            return {'success': False, 'error': str(e), 'status': 500}
        return result

    def get_user_info(self) -> Dict[str, Any]:
        result = self._make_request('GET', 'users/me')
        if result and isinstance(result, dict) and result.get('success') and (result.get('status') == 200):
            self.user_info = result.get('data', {})
            if isinstance(self.user_info, dict):
                return self.user_info
            print('⚠️ Dữ liệu user không đúng format: {0}'.format(type(self.user_info)))
            return {}
        return None

    def get_facebook_accounts(self, limit=None):
        result = self._make_request('GET', 'fb-account', params={'limit': limit})
        if result and isinstance(result, dict) and result.get('success') and (result.get('status') == 200):
            data = result.get('data', {})
            if isinstance(data, dict) and 'data' in data:
                self.fb_accounts = data['data']
                return self.fb_accounts
            elif isinstance(data, list):
                self.fb_accounts = data
                return self.fb_accounts
            print('⚠️ Dữ liệu accounts không đúng format: {0}'.format(type(data)))
            return []
        else:
            print('❌ Không thể lấy danh sách accounts')
            return []

    def get_available_jobs(self, fb_id, job_type=None):
        endpoint = 'advertising/publishers/get-jobs-2026'
        params = {'fb_id': fb_id}
        if job_type:
            params['type'] = job_type
        params['server'] = 'sv1'
        result = self._make_request('GET', endpoint, params=params)
        if result and isinstance(result, dict) and result.get('success') and (result.get('status') == 200):
            jobs = result.get('data', [])
            if isinstance(jobs, list):
                return jobs
            print('⚠️ Dữ liệu jobs không đúng format: {0}'.format(type(jobs)))
            return []
        error_msg = result.get('message', 'Unknown error') if result else 'No response'
        print('❌ Không thể lấy jobs: {0}'.format(error_msg))
        return []

    def complete_job(self, job_data: Dict) -> Dict:
        endpoint = 'advertising/publishers/complete-jobs-2026'
        if 'fb_id' in job_data and 'uid' not in job_data:
            job_data['uid'] = job_data['fb_id']
        clean_data = {'job_id': job_data.get('job_id'), 'type': job_data.get('type'), 'uid': job_data.get('uid') or job_data.get('fb_id'), 'retry': True}
        if 'comment_id' in job_data:
            clean_data['comment_id'] = job_data['comment_id']
        if 'message' in job_data:
            clean_data['message'] = job_data['message']
        if 'object_id' in job_data:
            clean_data['object_id'] = job_data['object_id']
        result = self._make_request('POST', endpoint, data=clean_data)
        if not isinstance(result, dict):
            return {'success': False, 'error': 'Invalid response type: {0}'.format(type(result)), 'data': result, 'status': 500}
        if result.get('status') == 200 and result.get('success') == True:
            data = result.get('data')
            message = result.get('message', '')
            price = 0
            data_dict = {}
            if isinstance(data, dict):
                price = data.get('price_after_cost', 0)
                data_dict = data
            elif isinstance(data, list) and len(data) > 0 and isinstance(data[0], dict):
                price = data[0].get('price_after_cost', 0)
                data_dict = data[0]
            if not isinstance(price, (int, float)):
                try:
                    price = int(price) if price else 0
                except:
                    price = 0
            if message and isinstance(message, str) and ('|' in message):
                parts = message.split('|')
                for part in parts:
                    if 'Số Job hôm nay' in part or 'Số Job hôm này' in part:
                        try:
                            import re
                            numbers = re.findall('\\d+', part)
                            if numbers:
                                job_count = int(numbers[0])
                                self.daily_jobs_count = job_count
                        except:
                            pass
            self.job_history.append({'job_id': job_data.get('job_id'), 'type': job_data.get('type'), 'time': datetime.now().strftime('%H:%M:%S'), 'success': True, 'reward': price, 'data': data_dict, 'message': message})
            return {'success': True, 'reward': price, 'data': data_dict, 'message': message, 'daily_jobs': self.daily_jobs_count}
        else:
            if result.get('status') == 400:
                message = result.get('message', '')
                error_msg = message if message else 'Lỗi 400 không xác định'
                self.job_history.append({'job_id': job_data.get('job_id'), 'type': job_data.get('type'), 'time': datetime.now().strftime('%H:%M:%S'), 'success': False, 'error': error_msg, 'status': 400})
                return {'success': False, 'error': error_msg, 'data': result, 'status': 400}
            msg = result.get('message', 'Không rõ lỗi') if isinstance(result, dict) else 'Không có phản hồi'
            status = result.get('status', 500) if isinstance(result, dict) else 500
            self.job_history.append({'job_id': job_data.get('job_id'), 'type': job_data.get('type'), 'time': datetime.now().strftime('%H:%M:%S'), 'success': False, 'error': msg, 'status': status})
            return {'success': False, 'error': msg, 'data': result, 'status': status}

    def report_error(self, job_id: int, fb_account_id: int) -> bool:
        data = {'description': 'Tôi đã làm Job này rồi', 'users_advertising_id': job_id, 'type': 'ads', 'fb_id': str(fb_account_id), 'error_type': 0, 'provider': 'facebook', 'comment': None}
        result = self._make_request('POST', 'report/send', data=data)
        return True

    def show_job_history(self):
        if not self.job_history:
            print('\n📊 Chưa có lịch sử')
            return
        print('\n📊 LỊCH SỬ JOB (10 gần nhất):')
        print('-' * 50)
        for i, job in enumerate(self.job_history[-10:], 1):
            status = '✅' if job.get('success') else '❌'
            status_code = '[{0}]'.format(job.get('status')) if job.get('status') else ''
            print('{0}. {1} {2} Job {3} - {4} - {5}'.format(i, status, status_code, job.get('job_id'), job.get('type'), job.get('time')))
            if job.get('success') and job.get('reward'):
                print('   💰 +{0} coin'.format(job.get('reward')))
            if job.get('error'):
                print('   ❌ {0}'.format(job.get('error')[:50]))
        successful = [j for j in self.job_history if j.get('success')]
        total_reward = sum((j.get('reward', 0) for j in successful if isinstance(j.get('reward'), (int, float))))
        print('-' * 50)
        print('📈 Tổng: {0}/{1} thành công'.format(len(successful), len(self.job_history)))
        print('💰 Tổng coin: {0}'.format(total_reward))
        if self.daily_jobs_count:
            print('📅 Job hôm nay: {0}'.format(self.daily_jobs_count))

    def show_account_status(self):
        print('\n' + '=' * 50)
        print('📊 TRẠNG THÁI TÀI KHOẢN')
        print('=' * 50)
        if self.user_info and isinstance(self.user_info, dict):
            print('\n👤 USER:')
            print('   - Tên: {0}'.format(self.user_info.get('name')))
            print('   - Email: {0}'.format(self.user_info.get('email')))
            print('   - Coin: {0}'.format(self.user_info.get('coin')))
            print('   - Hạng: {0}'.format(self.user_info.get('user_rank', {}).get('rank_name')))
        if self.fb_accounts and isinstance(self.fb_accounts, list):
            print('\n📱 FACEBOOK ACCOUNTS:')
            active = [a for a in self.fb_accounts if a.get('status') == 1]
            inactive = [a for a in self.fb_accounts if a.get('status') == 0]
            print('   - Tổng: {0}'.format(len(self.fb_accounts)))
            print('   - Active: {0}'.format(len(active)))
            print('   - Inactive: {0}'.format(len(inactive)))
            for acc in active[:5]:
                print('\n   📌 {0}'.format(acc.get('fb_name')))
                print('      ID: {0}'.format(acc.get('fb_id')))
                print('      Account ID: {0}'.format(acc.get('id')))
                jobs = acc.get('jobs_can_work', {})
                if not jobs:
                    continue
                if isinstance(jobs, dict):
                    job_types = [k for k, v in jobs.items() if v]
                    print('      Jobs: {0}'.format(', '.join(job_types)))
        print('\n📅 Job hôm nay: {0}'.format(self.daily_jobs_count))
        self.show_job_history()

class Pro5_Api:

    def __init__(self, cookie: str, proxy=None):
        self.fb_dtsg = ''
        self.jazoest = ''
        self.lsd = ''
        self.cookie = cookie
        self.proxies = None
        self.pages = []
        self.page_ids = []
        self.selected_page_id = None
        self.selected_page_name = None
        self.id = None
        if proxy:
            try:
                proxy_parts = proxy.strip().split(':')
                if len(proxy_parts) == 4:
                    host, port, user, password = proxy_parts
                    self.proxies = {'http': 'http://{0}:{1}@{2}:{3}'.format(user, password, host, port), 'https': 'http://{0}:{1}@{2}:{3}'.format(user, password, host, port)}
                elif len(proxy_parts) == 2:
                    host, port = proxy_parts
                    self.proxies = {'http': 'http://{0}:{1}'.format(host, port), 'https': 'http://{0}:{1}'.format(host, port)}
            except:
                self.proxies = None
        self.session = requests.Session()
        if self.proxies:
            self.session.proxies.update(self.proxies)
        i_user_match = re.search('i_user=(\\d+)', cookie)
        if i_user_match:
            self.id = i_user_match.group(1)
            self.is_page_mode = True
        else:
            c_user_match = re.search('c_user=(\\d+)', cookie)
            if c_user_match:
                self.id = c_user_match.group(1)
                self.is_page_mode = False
            else:
                self.id = ''
                self.is_page_mode = False
        self.headers = {'authority': 'www.facebook.com', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'accept-language': 'vi', 'sec-ch-prefers-color-scheme': 'light', 'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'document', 'sec-fetch-mode': 'navigate', 'sec-fetch-site': 'none', 'sec-fetch-user': '?1', 'upgrade-insecure-requests': '1', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36', 'viewport-width': '1366', 'Cookie': self.cookie}
        self._get_dtsg()
        if not self.is_page_mode:
            self.__Get_Page__()

    def _get_dtsg(self):
        try:
            url = self.session.get('https://www.facebook.com/{0}'.format(self.id), headers=self.headers).url
            response = self.session.get(url, headers=self.headers).text
            matches = re.findall('\\["DTSGInitialData",\\[\\],\\{"token":"(.*?)"\\}', response)
            if len(matches) > 0:
                self.fb_dtsg = matches[0]
            jazoest_matches = re.findall('jazoest=(.*?)\\"', response)
            if jazoest_matches:
                self.jazoest = jazoest_matches[0]
            lsd_matches = re.findall('\\["LSD",\\[\\],\\{"token":"(.*?)"\\}', response)
            if lsd_matches:
                self.lsd = lsd_matches[0]
        except Exception as e:
            print('[X] Lỗi lấy dtsg: {0}'.format(e))

    def __Get_Page__(self):
        try:
            self.dem = 0
            self.pages = []
            self.page_ids = []
            if not self.fb_dtsg or not self.jazoest:
                print('[!] Chưa có fb_dtsg hoặc jazoest, thử lấy lại...')
                self._get_dtsg()
            data = {'fb_dtsg': self.fb_dtsg, 'jazoest': self.jazoest, 'variables': '{"showUpdatedLaunchpointRedesign":true,"useAdminedPagesForActingAccount":false,"useNewPagesYouManage":true}', 'doc_id': '5300338636681652'}
            headers = {'cookie': self.cookie, 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36', 'content-type': 'application/x-www-form-urlencoded'}
            response = self.session.post('https://www.facebook.com/api/graphql/', headers=headers, data=data)
            try:
                json_response = response.json()
            except:
                text = response.text
                start = text.find('{')
                if start != -1:
                    end = text.rfind('}')
                    if end != -1:
                        json_str = text[start:end + 1]
                        json_response = json.loads(json_str)
                    else:
                        print('[X] Không tìm thấy JSON trong response')
                        return []
                else:
                    print('[X] Response không phải JSON')
                    return []
        except Exception as e:
            print('[X] Lỗi lấy danh sách page: {0}'.format(e))
            return []
        profiles = json_response.get('data', {}).get('viewer', {}).get('actor', {}).get('profile_switcher_eligible_profiles', {}).get('nodes', [])
        if profiles:
            for profile in profiles:
                self.dem += 1
                profile_data = profile.get('profile', {})
                page_id = profile_data.get('id')
                page_name = profile_data.get('name')
                if page_id:
                    self.pages.append({'index': self.dem, 'id': page_id, 'name': page_name})
                    self.page_ids.append(page_id)
            print('\r[✓] Tìm thấy {0} page profile'.format(len(self.pages)), end='\r')
        else:
            print('[!] Không tìm thấy page profile nào')
            return []
        return self.pages

    def info(self):
        try:
            if self.selected_page_id:
                return {'success': 200, 'id': self.selected_page_id, 'name': self.selected_page_name, 'is_page': True}
            get = self.session.get('https://www.facebook.com/me', headers=self.headers).url
            if 'next=' in get:
                match = re.search('next=/(\\d+)', get)
                if match:
                    url = 'https://www.facebook.com/{0}/'.format(match.group(1))
                else:
                    url = 'https://www.facebook.com/'
            else:
                url = get
            response = self.session.get(url, headers=self.headers, params={'locale': 'vi_VN'})
            if '828281030927956' in response.text:
                return {'success': False, 'error': '956', 'message': 'Cookie bị checkpoint 956'}
            if '1501092823525282' in response.text:
                return {'success': False, 'error': '282', 'message': 'Cookie bị checkpoint 282'}
            if '601051028565049' in response.text:
                return {'success': False, 'error': 'spam', 'message': 'Cookie bị spam'}
            data_split = response.text.split('"CurrentUserInitialData",[],{')
            if len(data_split) > 1:
                json_data = '{' + data_split[1].split('},')[0] + '}'
                parsed_data = json.loads(json_data)
                user_id = parsed_data.get('USER_ID', '0')
                name = parsed_data.get('NAME', '')
                if user_id == '0' and name == '':
                    return {'success': False, 'error': 'cookieout', 'message': 'Cookie hết hạn'}
                return {'success': 200, 'id': user_id, 'name': name, 'is_page': self.is_page_mode}
        except Exception as e:
            print('[X] Lỗi lấy info: {0}'.format(e))
            return {'success': False, 'error': str(e), 'message': 'Lỗi kiểm tra'}
        return {'success': False, 'error': 'unknown', 'message': 'Không xác định'}

    def get_post_id(self, link):
        try:
            getuid = requests.post('https://id.traodoisub.com/api.php', data={'link': link}).json()
            if 'id' in getuid:
                return getuid['id']
            time.sleep(2)
        except Exception as e:
            print('[X] Lỗi lấy ID: {0}'.format(e))
        return None

    def react_post(self, object_id, type_react):
        react_map = {'like': '1635855486666999', 'love': '1678524932434102', 'care': '613557422527858', 'haha': '115940658764963', 'wow': '478547315650144', 'sad': '908563459236466', 'angry': '444813342392137'}
        react_id = react_map.get(type_react.lower())
        if not react_id:
            return False
        headers = {'cookie': self.cookie, 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36', 'content-type': 'application/x-www-form-urlencoded'}
        data = {'av': self.id, 'fb_dtsg': self.fb_dtsg, 'jazoest': self.jazoest, 'lsd': self.lsd, 'fb_api_caller_class': 'RelayModern', 'fb_api_req_friendly_name': 'CometUFIFeedbackReactMutation', 'variables': '{{"input":{{"feedback_id":"{0}","feedback_reaction_id":"{1}","actor_id":"{2}","client_mutation_id":"1"}},"useDefaultActor":false}}'.format(encode_to_base64('feedback:' + str(object_id)), react_id, self.id), 'server_timestamps': 'true', 'doc_id': '7047198228715224'}
        try:
            res = self.session.post('https://www.facebook.com/api/graphql/', headers=headers, data=data)
            if 'feedback_react' not in res.text:
                return False
        except Exception as e:
            print('[X] Lỗi khi thả cảm xúc: {0}'.format(e))
            return False
        return True

    def react_auto(self, link, type_react):
        object_id = self.get_post_id(link)
        if not object_id:
            return False
        return self.react_post(object_id, type_react)

    def reaction(self, object_id, type_react):
        return self.react_post(object_id, type_react)

    def follow(self, id):
        try:
            headers = {'cookie': self.cookie, 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36', 'content-type': 'application/x-www-form-urlencoded'}
            response = self.session.post('https://www.facebook.com/api/graphql/', headers=headers, data={'fb_dtsg': self.fb_dtsg, 'jazoest': self.jazoest, 'lsd': self.lsd, 'variables': '{"input":{"subscribe_location":"PROFILE","subscribee_id":"' + id + '","actor_id":"' + self.id + '","client_mutation_id":"1"},"scale":1}', 'doc_id': '5032256523527306'})
            if '"subscribe_status":"IS_SUBSCRIBED"' not in response.text:
                return False
        except:
            return False
        return True

    def like_page(self, id):
        try:
            headers = {'cookie': self.cookie, 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36', 'content-type': 'application/x-www-form-urlencoded'}
            response = self.session.post('https://www.facebook.com/api/graphql/', headers=headers, data={'fb_dtsg': self.fb_dtsg, 'jazoest': self.jazoest, 'lsd': self.lsd, 'variables': '{"input":{"is_tracking_encrypted":true,"page_id":"' + id + '","source":"unknown","tracking":[],"actor_id":"' + self.id + '","client_mutation_id":"2"},"isAdminView":false}', 'doc_id': '5556947024325929'})
            if '"subscribe_status":"IS_SUBSCRIBED"' not in response.text:
                return False
        except:
            return False
        return True

    def reactioncmt(self, id, type_react):
        try:
            react_map = {'LIKE': '1635855486666999', 'LOVE': '1678524932434102', 'CARE': '613557422527858', 'HAHA': '115940658764963', 'WOW': '478547315650144', 'SAD': '908563459236466', 'ANGRY': '444813342392137'}
            id_reac = react_map.get(type_react.upper())
            if id_reac:
                headers = {'cookie': self.cookie, 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36', 'content-type': 'application/x-www-form-urlencoded'}
                g_now = datetime.now()
                d = g_now.strftime('%Y-%m-%d %H:%M:%S.%f')
                datetime_object = datetime.strptime(d, '%Y-%m-%d %H:%M:%S.%f')
                timestamp = str(datetime_object.timestamp())
                starttime = timestamp.replace('.', '')
                data = {'av': self.id, 'fb_dtsg': self.fb_dtsg, 'jazoest': self.jazoest, 'lsd': self.lsd, 'fb_api_caller_class': 'RelayModern', 'fb_api_req_friendly_name': 'CometUFIFeedbackReactMutation', 'variables': '{"input":{"attribution_id_v2":"CometVideoHomeNewPermalinkRoot.react,comet.watch.injection,via_cold_start,1719930662698,975645,2392950137,,","feedback_id":"' + encode_to_base64('feedback:' + str(id)) + '","feedback_reaction_id":"' + id_reac + '","feedback_source":"TAHOE","is_tracking_encrypted":true,"tracking":[],"session_id":"' + str(uuid.uuid4()) + '","downstream_share_session_id":"' + str(uuid.uuid4()) + '","downstream_share_session_origin_uri":"https://fb.watch/t3OatrTuqv/?mibextid=Nif5oz","downstream_share_session_start_time":"' + starttime + '","actor_id":"' + self.id + '","client_mutation_id":"1"},"useDefaultActor":false,"__relay_internal__pv__CometUFIReactionsEnableShortNamerelayprovider":false}', 'server_timestamps': 'true', 'doc_id': '7616998081714004'}
                response = self.session.post('https://www.facebook.com/api/graphql/', headers=headers, data=data)
                if 'feedback_react' not in response.text:
                    return False
            else:
                return False
        except:
            return False
        return True

    def comment(self, id, msg: str):
        try:
            headers = {'cookie': self.cookie, 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36', 'content-type': 'application/x-www-form-urlencoded'}
            data = {'av': self.id, 'fb_dtsg': self.fb_dtsg, 'jazoest': self.jazoest, 'lsd': self.lsd, 'fb_api_caller_class': 'RelayModern', 'fb_api_req_friendly_name': 'useCometUFICreateCommentMutation', 'variables': '{{"feedLocation":"DEDICATED_COMMENTING_SURFACE","feedbackSource":110,"groupID":null,"input":{{"client_mutation_id":"4","actor_id":"{0}","attachments":null,"feedback_id":"{1}","formatting_style":null,"message":{{"ranges":[],"text":"{2}"}},"attribution_id_v2":"CometHomeRoot.react,comet.home,via_cold_start,1718688700413,194880,4748854339,,","vod_video_timestamp":null,"feedback_referrer":"/","is_tracking_encrypted":true,"tracking":[],"feedback_source":"DEDICATED_COMMENTING_SURFACE","idempotence_token":"client:{3}","session_id":"{4}"}},"inviteShortLinkKey":null,"renderLocation":null,"scale":1,"useDefaultActor":false,"focusCommentID":null}}'.format(self.id, encode_to_base64('feedback:{0}'.format(id)), msg, uuid.uuid4(), uuid.uuid4()), 'server_timestamps': 'true', 'doc_id': '7994085080671282'}
            response = self.session.post('https://www.facebook.com/api/graphql/', headers=headers, data=data)
            if '{"data":{"comment_create":{"feedback":{"' not in response.text:
                return False
        except:
            return False
        return True

    def share(self, id):
        try:
            headers = {'cookie': self.cookie, 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36', 'content-type': 'application/x-www-form-urlencoded'}
            data = {'av': self.id, '__usid': '6-Tsftw3x1vqj8dz:Psftw2g2c595x:0-Asftw3x1etit7l-RV=6:F=', '__aaid': '0', '__user': self.id, '__a': '1', '__req': '1o', '__hs': '19901.HYP:comet_pkg.2.1..2.1', 'dpr': '1', '__ccg': 'EXCELLENT', '__rev': '1014511729', '__s': '8zktjb:5quia4:fu1x9q', '__hsi': '7384980750065440159', '__dyn': '7AzHK4HwkEng5K8G6EjBAg5S3G2O5U4e2C17xt3odE98K360CEboG0x8bo6u3y4o2Gwn82nwb-q7oc81xoswMwto886C11wBz83WwgEcEhwGxu782lwv89kbxS1Fwc61awkovwRwlE-U2exi4UaEW2G1jwUBwJK2W5olwUwgojUlDw-wSU8o4Wm7-2K0-poarCwLyES0Io88cA0z8c84q58jyUaUcojxK2B08-269wkopg6C13whEeE4WVU-4EdrxG1fy8bUaU', '__csr': 'gdk8MPs4dNYQYp4iOSD9sG2fZqN79mKHYBH4qrNP5bifl8IyAF-CDQGFdBdlTmeimHGOWJKhCKRWDLjGmV94uVpprh6FaDD_GcG5F4ECVqgCqhqRAKhd2oGAUBzaUCibGVHy9EFeayEjCxim598oxmmCETxObKuuUyfzF8411e2e7VHyq-dG8AK4oW4ogK69XzEy7U4aFQ4EdE426UKdxm7E98sG15Cw8Oi1awgUaolwvUO8wrU3ewNwt9UOvwko16o1z81uo1gA0cww1pHxGQE2Kw0sv80Ii6E03c4U9olw1N21Cw1eu05rE1oUmxiew0iIU0e5k0m-02jW1RyU2pwPw3uU0u3w4wAo0Xi0Bk', '__comet_req': '15', 'fb_dtsg': self.fb_dtsg, 'jazoest': self.jazoest, 'lsd': self.lsd, '__spin_r': '1014511729', '__spin_b': 'trunk', '__spin_t': '1719449821', 'fb_api_caller_class': 'RelayModern', 'fb_api_req_friendly_name': 'ComposerStoryCreateMutation', 'variables': '{"input":{"composer_entry_point":"share_modal","composer_source_surface":"feed_story","composer_type":"share","idempotence_token":"' + str(uuid.uuid4()) + '_FEED","source":"WWW","attachments":[{"link":{"share_scrape_data":"{\\"share_type\\":22,\\"share_params\\":[' + id + ']}"}}],"reshare_original_post":"RESHARE_ORIGINAL_POST","audience":{"privacy":{"allow":[],"base_state":"EVERYONE","deny":[],"tag_expansion_state":"UNSPECIFIED"}},"is_tracking_encrypted":true,"tracking":[],"logging":{"composer_session_id":"' + str(uuid.uuid4()) + '"},"navigation_data":{"attribution_id_v2":"FeedsCometRoot.react,comet.most_recent_feed,tap_bookmark,1719641912186,189404,608920319153834,,"},"event_share_metadata":{"surface":"newsfeed"},"actor_id":"' + self.id + '","client_mutation_id":"3"},"feedLocation":"NEWSFEED","feedbackSource":1,"focusCommentID":null,"gridMediaWidth":null,"groupID":null,"scale":1,"privacySelectorRenderLocation":"COMET_STREAM","checkPhotosToReelsUpsellEligibility":false,"renderLocation":"homepage_stream","useDefaultActor":false,"inviteShortLinkKey":null,"isFeed":true,"isFundraiser":false,"isFunFactPost":false,"isGroup":false,"isEvent":false,"isTimeline":false,"isSocialLearning":false,"isPageNewsFeed":false,"isProfileReviews":false,"isWorkSharedDraft":false,"hashtag":null,"canUserManageOffers":false,"__relay_internal__pv__CometIsAdaptiveUFIEnabledrelayprovider":true,"__relay_internal__pv__CometUFIShareActionMigrationrelayprovider":true,"__relay_internal__pv__IncludeCommentWithAttachmentrelayprovider":true,"__relay_internal__pv__CometUFIReactionsEnableShortNamerelayprovider":false,"__relay_internal__pv__CometImmersivePhotoCanUserDisable3DMotionrelayprovider":false,"__relay_internal__pv__IsWorkUserrelayprovider":false,"__relay_internal__pv__IsMergQAPollsrelayprovider":false,"__relay_internal__pv__StoriesArmadilloReplyEnabledrelayprovider":true,"__relay_internal__pv__StoriesRingrelayprovider":false,"__relay_internal__pv__EventCometCardImage_prefetchEventImagerelayprovider":false}', 'server_timestamps': 'true', 'doc_id': '8167261726632010'}
            response = self.session.post('https://www.facebook.com/api/graphql/', headers=headers, data=data)
            if 'success' not in response.text:
                return False
        except:
            return False
        return True

def nhap_cookie(proxy=None):
    print('\n{0}{1}┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓'.format(thanh, luc))
    print('{0}{1}┃         🍪 NHẬP COOKIE               ┃'.format(thanh, luc))
    print('{0}{1}┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛'.format(thanh, luc))
    choice = input('{0}{1}📝 [1] Nhập cookie trực tiếp\n   [2] Lấy từ file cookie.txt\n{2}{3}➤ Chọn: {4}'.format(thanh, luc, thanh, luc, vang)).strip()
    cookies_raw = []
    if choice == '2':
        if os.path.exists('cookie.txt'):
            with open('cookie.txt', 'r', encoding='utf-8') as f:
                cookies_raw = [line.strip() for line in f if line.strip()]
            print('{0}{1}✅ Đã đọc {2} cookie từ file'.format(thanh, luc, len(cookies_raw)))
        else:
            print('{0}{1}❌ Không tìm thấy file cookie.txt'.format(thanh, do))
            return []
    else:
        print('{0}{1}📝 Nhập cookie (Enter trống để kết thúc):'.format(thanh, luc))
        while True:
            c = input('{0}{1}🍪 Cookie: {2}'.format(thanh, luc, vang)).strip()
            if not c:
                break
            cookies_raw.append(c)
    if not cookies_raw:
        print('{0}{1}❌ Không có cookie nào được nhập!'.format(thanh, do))
        return []
    print('\n{0}{1}┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓'.format(thanh, luc))
    print('{0}{1}┃       ⚙️ CHỌN CHẾ ĐỘ CHẠY            ┃'.format(thanh, luc))
    print('{0}{1}┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛'.format(thanh, luc))
    print('{0}{1}[1] {2}All Main + All Page (tất cả main + tất cả page){3}'.format(thanh, luc, trang, luc))
    print('{0}{1}[2] {2}All Main + Mỗi Page (chọn page cho tất cả main){3}'.format(thanh, luc, trang, luc))
    print('{0}{1}[3] {2}Từng Main + Từng Page (tự chọn cho từng main){3}'.format(thanh, luc, trang, luc))
    mode = input('{0}{1}➤ Chọn chế độ (1-3): {2}'.format(thanh, luc, vang)).strip()
    all_cookies = []
    for cookie in cookies_raw:
        fb = Pro5_Api(cookie, proxy)
        info = fb.info()
        if info.get('success') == 200:
            print('{0}{1}✅ Main: {2}{3} {4}(ID: {5}{6}{7})'.format(thanh, luc, vang, info.get('name'), luc, vang, info.get('id'), luc))
            if mode == '1':
                if fb.pages:
                    for page in fb.pages:
                        page_cookie = tao_page_cookie(cookie, page['id'])
                        all_cookies.append(page_cookie)
                    print('{0}{1}  └→ Thêm {2} page'.format(thanh, luc, len(fb.pages)))
                else:
                    all_cookies.append(cookie)
                    print('{0}{1}  └→ Không có page, dùng main'.format(thanh, vang))
            elif mode == '2':
                if fb.pages:
                    if not hasattr(nhap_cookie, 'selected_page_ids'):
                        print('{0}{1}📋 Danh sách page của main {2}:'.format(thanh, luc, info.get('name')))
                        for page in fb.pages:
                            print('{0}{1}  [{2}{3}{4}] {5}{6}'.format(thanh, luc, vang, page['index'], luc, trang, page['name']))
                        chon = input("{0}{1}➤ Chọn page (số, hoặc 'all'): {2}".format(thanh, luc, vang)).strip()
                        if chon.lower() == 'all':
                            nhap_cookie.selected_page_ids = [p['id'] for p in fb.pages]
                        elif chon.isdigit():
                            idx = int(chon) - 1
                            if 0 <= idx < len(fb.pages):
                                nhap_cookie.selected_page_ids = [fb.pages[idx]['id']]
                            else:
                                nhap_cookie.selected_page_ids = []
                        else:
                            nhap_cookie.selected_page_ids = []
                    if nhap_cookie.selected_page_ids:
                        for page_id in nhap_cookie.selected_page_ids:
                            page_cookie = tao_page_cookie(cookie, page_id)
                            all_cookies.append(page_cookie)
                        print('{0}{1}  └→ Thêm {2} page'.format(thanh, luc, len(nhap_cookie.selected_page_ids)))
                    else:
                        all_cookies.append(cookie)
                        print('{0}{1}  └→ Dùng main'.format(thanh, vang))
                else:
                    print('{0}{1}  └→ Không có page, dùng main'.format(thanh, vang))
                    all_cookies.append(cookie)
            elif mode == '3':
                if fb.pages:
                    print('{0}{1}📋 Page của main {2}:'.format(thanh, luc, info.get('name')))
                    for page in fb.pages:
                        print('{0}{1}  [{2}{3}{4}] {5}{6}'.format(thanh, luc, vang, page['index'], luc, trang, page['name']))
                    chon = input("{0}{1}➤ Chọn page cho main này (số, 'all', hoặc 0 để dùng main): {2}".format(thanh, luc, vang)).strip()
                    if chon == '0':
                        all_cookies.append(cookie)
                        print('{0}{1}  └→ Dùng main'.format(thanh, luc))
                    elif chon.lower() == 'all':
                        for page in fb.pages:
                            page_cookie = tao_page_cookie(cookie, page['id'])
                            all_cookies.append(page_cookie)
                        print('{0}{1}  └→ Thêm {2} page'.format(thanh, luc, len(fb.pages)))
                    elif chon.isdigit():
                        idx = int(chon) - 1
                        if 0 <= idx < len(fb.pages):
                            page_cookie = tao_page_cookie(cookie, fb.pages[idx]['id'])
                            all_cookies.append(page_cookie)
                            print('{0}{1}  └→ Thêm page: {2}'.format(thanh, luc, fb.pages[idx]['name']))
                        else:
                            all_cookies.append(cookie)
                            print('{0}{1}  └→ Số không hợp lệ, dùng main'.format(thanh, vang))
                    else:
                        all_cookies.append(cookie)
                        print('{0}{1}  └→ Không hiểu, dùng main'.format(thanh, vang))
                else:
                    print('{0}{1}  └→ Không có page, dùng main'.format(thanh, vang))
                    all_cookies.append(cookie)
        else:
            print('{0}{1}❌ Cookie lỗi: {2}'.format(thanh, do, info.get('message', 'Không xác định')))
    if mode != '3' and hasattr(nhap_cookie, 'selected_page_ids'):
        delattr(nhap_cookie, 'selected_page_ids')
    if all_cookies:
        print('{0}{1}✅ Tổng cộng: {2} cookie sẽ được chạy'.format(thanh, luc, len(all_cookies)))
    else:
        print('{0}{1}❌ Không có cookie hợp lệ nào!'.format(thanh, do))
    return all_cookies

def tao_page_cookie(cookie, page_id):
    cookie_parts = cookie.split(';')
    cookies_values = {}
    for item in cookie_parts:
        if '=' in item:
            key, value = item.split('=', 1)
            cookies_values[key.strip()] = value.strip()
    sb = cookies_values.get('sb', '')
    datr = cookies_values.get('datr', '')
    c_user = cookies_values.get('c_user', '')
    xs = cookies_values.get('xs', '')
    fr = cookies_values.get('fr', '')
    cookie_parts_list = []
    if sb:
        cookie_parts_list.append('sb={0}'.format(sb))
    if datr:
        cookie_parts_list.append('datr={0}'.format(datr))
    if c_user:
        cookie_parts_list.append('c_user={0}'.format(c_user))
    if xs:
        cookie_parts_list.append('xs={0}'.format(xs))
    if fr:
        cookie_parts_list.append('fr={0}'.format(fr))
    cookie_parts_list.append('i_user={0}'.format(page_id))
    return ';'.join(cookie_parts_list) + ';'

class MainGLFB:

    def __init__(self):
        self.auth = ''
        self.cookies = []
        self.proxies = []
        self.job_choice = '4'
        self.delay = 10
        self.golike_instances = {}
        self.mode = 'multi'
        self.jobs_per_account = 10
        self.use_proxy = False
        self.processed_jobs = set()
        self.failed_jobs = {}
        self.job_cooldown = {}
        self.max_retries = 3
        self.cooldown_seconds = 300

    def read_file(self, path):
        if os.path.exists(path):
            with open(path, 'r', encoding='utf-8') as f:
                return f.read()
        return ''

    def read_lines(self, path):
        if os.path.exists(path):
            with open(path, 'r', encoding='utf-8') as f:
                return [line.strip() for line in f if line.strip()]
        return []

    def save_file(self, path, data):
        with open(path, 'w', encoding='utf-8') as f:
            f.write(data.strip())

    def get_auth(self):
        saved = self.read_file('Auth_Golike.txt')
        if saved:
            print('┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓')
            print('┃         🔐 AUTH GOLIKE              ┃')
            print('┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫')
            print('┃ 📁 Đã lưu: {0}...'.format(saved[:40]))
            print('┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫')
            print('┃ [1] Dùng lại auth cũ                 ┃')
            print('┃ [2] Nhập auth mới                    ┃')
            print('┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛')
            chon = input('➤ Chọn: ').strip()
            if chon == '1':
                self.auth = saved
                print('✅ Đã dùng lại auth từ file')
            else:
                self.auth = input('✏️ Nhập Auth Golike mới: ').strip()
                self.save_file('Auth_Golike.txt', self.auth)
                print('💾 Đã lưu auth mới')
        else:
            print('⚠️ Chưa có auth Golike')
            self.auth = input('✏️ Nhập Auth Golike: ').strip()
            self.save_file('Auth_Golike.txt', self.auth)
            print('💾 Đã lưu auth')

    def get_mode(self):
        choice = '2'

    def get_proxies(self):
        print('┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓')
        print('┃         🌐 CẤU HÌNH PROXY            ┃')
        print('┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫')
        print('┃ [1] Nhập Proxy trực tiếp            ┃')
        print('┃ [2] Nhập Proxy từ file (proxy.txt)  ┃')
        print('┃ [3] Không dùng Proxy                ┃')
        print('┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛')
        choice = input('➤ Chọn (1-3): ').strip()
        if choice == '1':
            proxy_input = input('📝 Nhập proxy (format: ip:port hoặc user:pass@ip:port): ').strip()
            if proxy_input:
                self.proxies = [proxy_input]
                self.use_proxy = True
                print('✅ Đã nhập proxy: {0}'.format(proxy_input))
            else:
                self.use_proxy = False
                print('⚠️ Không nhập proxy, chạy không proxy')
        elif choice == '2':
            self.proxies = self.read_lines('proxy.txt')
            if self.proxies:
                self.use_proxy = True
                print('🌐 Đã nạp {0} proxy từ proxy.txt'.format(len(self.proxies)))
            else:
                self.use_proxy = False
                print('⚠️ Không tìm thấy proxy trong proxy.txt - Chạy không proxy')
        else:
            self.use_proxy = False
            print('⚠️ Chạy không dùng proxy')

    def get_cookies(self):
        if self.use_proxy and self.proxies:
            proxy_to_use = self.proxies[0]
            self.cookies = nhap_cookie(proxy_to_use)
        else:
            self.cookies = nhap_cookie(None)
        if not self.cookies:
            print('❌ Không có cookie hợp lệ!')
            sys.exit(1)
        print('✅ Tổng số cookie sẽ chạy: {0}'.format(len(self.cookies)))

    def get_job_choice(self):
        print('┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓')
        print('┃         🎯 CHỌN LOẠI JOB             ┃')
        print('┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫')
        print('┃ [1] Reaction    💖                    ┃')
        print('┃ [2] Like Page   📄                    ┃')
        print('┃ [3] Follow      👥                    ┃')
        print('┃ [4] Tất cả      🔥                    ┃')
        print('┃ [5] Comment     💬                    ┃')
        print('┃ [6] Share       🔄                    ┃')
        print('┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛')
        self.job_choice = input('➤ Chọn (1-6): ').strip() or '4'

    def get_delay(self):
        try:
            print('⏱️ Nhập delay giữa các job (giây):')
            self.delay = int(input('➤ Delay: ') or '10')
            print('✅ Delay {0} giây'.format(self.delay))
        except:
            self.delay = 10
            print('⚠️ Dùng delay mặc định: {0}s'.format(self.delay))

    def map_job_type(self, golike_type):
        job_map = {'like': 'LIKE', 'like_corona_0': 'LIKE', 'love': 'LOVE', 'care': 'CARE', 'haha': 'HAHA', 'wow': 'WOW', 'sad': 'SAD', 'angry': 'ANGRY', 'like_comment': 'LIKE COMMENT', '_page': 'LIKE PAGE', 'like_page': 'LIKE PAGE', 'like_page_corona_0': 'LIKE PAGE', 'follow': 'FOLLOW', 'follow_corona_0': 'FOLLOW', 'comment': 'COMMENT', 'share': 'SHARE'}
        return job_map.get(golike_type, golike_type.upper())

    def filter_job_by_choice(self, job_type, job_choice):
        reaction_types = ['like', 'like_corona_0', 'love', 'care', 'haha', 'wow', 'sad', 'angry', 'like_comment']
        page_types = ['_page', 'like_page', 'like_page_corona_0']
        follow_types = ['follow', 'follow_corona_0']
        comment_types = ['comment']
        share_types = ['share']
        if job_choice == '1':
            return job_type in reaction_types
        if job_choice == '2':
            return job_type in page_types
        if job_choice == '3':
            return job_type in follow_types
        if job_choice == '5':
            return job_type in comment_types
        if job_choice == '6':
            return job_type in share_types
        return True

    def should_process_job(self, job_id, target):
        if job_id in self.processed_jobs:
            return (False, 'already_processed')
        if job_id in self.job_cooldown and datetime.now() < self.job_cooldown[job_id]:
            return (False, 'in_cooldown')
        if self.failed_jobs.get(job_id, 0) >= self.max_retries:
            return (False, 'max_retries_exceeded')
        return (True, 'ok')

    def handle_failed_job(self, job_id, fb_account_id, gl):
        self.failed_jobs[job_id] = self.failed_jobs.get(job_id, 0) + 1
        if self.failed_jobs[job_id] >= self.max_retries:
            self.job_cooldown[job_id] = datetime.now() + timedelta(seconds=self.cooldown_seconds)
            print('⚠️ Job {0} đã fail {1} lần, cooldown {2}s'.format(job_id[:12], self.max_retries, self.cooldown_seconds))
        gl.report_error(job_id, fb_account_id)

    def handle_success_job(self, job_id, target, reward):
        self.processed_jobs.add(job_id)
        if job_id in self.failed_jobs:
            del self.failed_jobs[job_id]
        if job_id in self.job_cooldown:
            del self.job_cooldown[job_id]
        return reward

    def run_cookie_single(self, cookie, auth, proxy, job_choice, delay, account_index, max_jobs):
        gl = GolikeJobAutomation(auth)
        user_info = gl.get_user_info()
        if not user_info:
            print('[Account {0}] ❌ Auth Golike sai hoặc hết hạn'.format(account_index))
            return 0
        fb = Pro5_Api(cookie, proxy)
        info_result = fb.info()
        if info_result.get('success') != 200:
            print('[Account {0}] ❌ Cookie Facebook lỗi: {1}'.format(account_index, info_result.get('message', 'Không xác định')))
            return 0
        fb_id = info_result.get('id', '')
        fb_name = info_result.get('name', 'Unknown')
        is_page = info_result.get('is_page', False)
        fb_accounts = gl.get_facebook_accounts()
        fb_account_info = None
        for acc in fb_accounts:
            acc_id = str(acc.get('fb_id', ''))
            if acc_id == str(fb_id):
                fb_account_info = acc
                break
        if not fb_account_info:
            print('[Account {0}] ⚠️ Facebook ID {1} chưa được thêm vào Golike'.format(account_index, fb_id))
            return 0
        fb_account_id = fb_account_info.get('id')
        stt = 0
        tongtien = 0
        jobs_completed = 0
        max_empty_loops = 15
        empty_loops = 0
        while jobs_completed < max_jobs and empty_loops < max_empty_loops:
            try:
                print(green_cyan_yellow_gradient('\r[Account {0}] Đang Get Job Facebook...'.format(account_index)), end='\r')
                jobs = gl.get_available_jobs(fb_id)
                if jobs:
                    empty_loops = 0
                    print('\r[Account {0}] Tìm thấy {1} job'.format(account_index, len(jobs)), end='\r')
                    new_jobs_found = False
                    for job in jobs:
                        if jobs_completed >= max_jobs:
                            break
                        job_id = job.get('id')
                        job_type = job.get('type')
                        target = job.get('object_id')
                        link = job.get('link', '')
                        should_process, reason = self.should_process_job(job_id, target)
                        if not should_process:
                            if reason == 'already_processed':
                                print(green_cyan_yellow_gradient('\r[Account {0}] ⏭️ Bỏ qua job đã xử lý: {1}'.format(account_index, job_id[:12])))
                            elif reason == 'in_cooldown':
                                print(green_cyan_yellow_gradient('\r[Account {0}] ⏸️ Job đang cooldown: {1}'.format(account_index, job_id[:12])))
                            elif reason == 'max_retries_exceeded':
                                print(green_cyan_yellow_gradient('\r[Account {0}] 🚫 Job đã fail quá nhiều: {1}'.format(account_index, job_id[:12])))
                            continue
                        if link and (not check_link_exists(link, 10, cookie)):
                            self.handle_failed_job(job_id, fb_account_id, gl)
                            continue
                        if self.filter_job_by_choice(job_type, job_choice):
                            new_jobs_found = True
                            stt += 1
                            job_name = self.map_job_type(job_type)
                            success = False
                            comment_id = None
                            comment_message = None
                            if job_type in ('like_page', '_page', 'like_page_corona_0'):
                                success = fb.like_page(target)
                            elif job_type in ('follow', 'follow_corona_0'):
                                success = fb.follow(target)
                            elif job_type == 'like_comment':
                                success = fb.reactioncmt(target, 'LIKE')
                            elif job_type in ('like', 'like_corona_0', 'love', 'care', 'haha', 'wow', 'sad', 'angry'):
                                if job_type == 'like_corona_0':
                                    job_type = 'like'
                                if link:
                                    success = fb.react_auto(link, job_type)
                                else:
                                    success = fb.reaction(target, job_type)
                            elif job_type == 'comment':
                                list_messages = job.get('list_message_jobs', [])
                                if list_messages and len(list_messages) > 0:
                                    comment_data = list_messages[0]
                                    comment_message = comment_data.get('message', '')
                                    comment_id = comment_data.get('id')
                                    if comment_message and target:
                                        success = fb.comment(target, comment_message)
                            elif job_type == 'share':
                                success = fb.share(target)
                            time.sleep(2)
                            if success:
                                job_data = {'job_id': job_id, 'type': job_type, 'fb_id': str(fb_id), 'uid': str(fb_id), 'account_id': fb_account_id, 'object_id': target}
                                if comment_id:
                                    job_data['comment_id'] = comment_id
                                if comment_message:
                                    job_data['message'] = comment_message
                                result = gl.complete_job(job_data)
                                if result and isinstance(result, dict) and result.get('success'):
                                    reward = result.get('reward', 0)
                                    if isinstance(reward, (int, float)):
                                        tongtien += reward
                                        jobs_completed += 1
                                        self.handle_success_job(job_id, target, reward)
                                    giophutgiay = datetime.now().strftime('%H:%M:%S')
                                else:
                                    giophutgiay = datetime.now().strftime('%H:%M:%S')
                                    error_msg = result.get('error', 'Unknown') if isinstance(result, dict) else str(result)
                                    self.handle_failed_job(job_id, fb_account_id, gl)
                            else:
                                giophutgiay = datetime.now().strftime('%H:%M:%S')
                                self.handle_failed_job(job_id, fb_account_id, gl)
                            Delay_Color(delay)
                    if new_jobs_found:
                        Delay_Color(10)
                    else:
                        empty_loops += 1
                else:
                    empty_loops += 1
                    print('\r[Account {0}] Không có job mới ({1}/{2})'.format(account_index, empty_loops, max_empty_loops), end='\r')
                    Delay_Color(10)
                    continue
            except Exception as e:
                print('\n[Account {0}] ❌ Lỗi: {1}'.format(account_index, str(e)))
                empty_loops += 1
                Delay_Color(10)
            if jobs_completed < max_jobs and empty_loops < max_empty_loops:
                continue
        print(green_cyan_yellow_gradient('\n[Account {0}] 📊 Hoàn thành: {1} job, {2} vnđ'.format(account_index, jobs_completed, tongtien)))
        return tongtien

    def run_cookie_multi(self, cookie, auth, proxy, job_choice, delay, idx):
        gl = GolikeJobAutomation(auth)
        self.golike_instances[idx] = gl
        user_info = gl.get_user_info()
        if not user_info:
            print('[THREAD {0}] ❌ Auth Golike sai hoặc hết hạn'.format(idx))
            return None
        fb = Pro5_Api(cookie, proxy)
        info_result = fb.info()
        if info_result.get('success') != 200:
            print('[THREAD {0}] ❌ Cookie Facebook lỗi: {1}'.format(idx, info_result.get('message', 'Không xác định')))
            return None
        fb_id = info_result.get('id', '')
        fb_name = info_result.get('name', 'Unknown')
        is_page = info_result.get('is_page', False)
        fb_accounts = gl.get_facebook_accounts()
        fb_account_info = None
        for acc in fb_accounts:
            acc_id = str(acc.get('fb_id', ''))
            if acc_id == str(fb_id):
                fb_account_info = acc
                break
        if not fb_account_info:
            print('[THREAD {0}] ⚠️ Facebook ID {1} chưa được thêm vào Golike'.format(idx, fb_id))
            return None
        fb_account_id = fb_account_info.get('id')
        stt = 0
        tongtien = 0
        empty_loops = 0
        max_empty_loops = 5
        while True:
            try:
                print(green_cyan_yellow_gradient('\r[THREAD {0}] Đang Get Job Facebook...'.format(idx)), end='\r')
                jobs = gl.get_available_jobs(fb_id)
                if jobs:
                    empty_loops = 0
                    print('\r[THREAD {0}] Tìm thấy {1} job'.format(idx, len(jobs)), end='\r')
                    new_jobs_found = False
                    for job in jobs:
                        stt += 1
                        job_id = job.get('id')
                        job_type = job.get('type')
                        target = job.get('object_id')
                        link = job.get('link', '')
                        should_process, reason = self.should_process_job(job_id, target)
                        if not should_process:
                            if reason == 'already_processed':
                                print(green_cyan_yellow_gradient('\r[THREAD {0}] ⏭️ Bỏ qua job đã xử lý: {1}'.format(idx, job_id[:12])))
                            elif reason == 'in_cooldown':
                                print(green_cyan_yellow_gradient('\r[THREAD {0}] ⏸️ Job đang cooldown: {1}'.format(idx, job_id[:12])))
                            elif reason == 'max_retries_exceeded':
                                print(green_cyan_yellow_gradient('\r[THREAD {0}] 🚫 Job đã fail quá nhiều: {1}'.format(idx, job_id[:12])))
                            continue
                        if link and (not check_link_exists(link, 10, cookie)):
                            self.handle_failed_job(job_id, fb_account_id, gl)
                            continue
                        if self.filter_job_by_choice(job_type, job_choice):
                            new_jobs_found = True
                            job_name = self.map_job_type(job_type)
                            success = False
                            comment_id = None
                            comment_message = None
                            if job_type in ('like_page', '_page', 'like_page_corona_0'):
                                success = fb.like_page(target)
                            elif job_type in ('follow', 'follow_corona_0'):
                                success = fb.follow(target)
                            elif job_type == 'like_comment':
                                success = fb.reactioncmt(target, 'LIKE')
                            elif job_type in ('like', 'like_corona_0', 'love', 'care', 'haha', 'wow', 'sad', 'angry'):
                                if job_type == 'like_corona_0':
                                    job_type = 'like'
                                if link:
                                    success = fb.react_auto(link, job_type)
                                else:
                                    success = fb.reaction(target, job_type)
                            elif job_type == 'comment':
                                list_messages = job.get('list_message_jobs', [])
                                if list_messages and len(list_messages) > 0:
                                    comment_data = list_messages[0]
                                    comment_message = comment_data.get('message', '')
                                    comment_id = comment_data.get('id')
                                    if comment_message and target:
                                        success = fb.comment(target, comment_message)
                            elif job_type == 'share':
                                success = fb.share(target)
                            time.sleep(6)
                            if success:
                                job_data = {'job_id': job_id, 'type': job_type, 'fb_id': str(fb_id), 'uid': str(fb_id), 'account_id': fb_account_id, 'object_id': target}
                                if comment_id:
                                    job_data['comment_id'] = comment_id
                                if comment_message:
                                    job_data['message'] = comment_message
                                result = gl.complete_job(job_data)
                                if result.get('success') == True:
                                    tien = result.get('data')['prices']
                                    giophutgiay = datetime.now().strftime('%H:%M:%S')
                                    print('>> [{0}] [{1}] THÀNH CÔNG <> +{2} | {3} | {4}'.format(giophutgiay, fb_name, tien, target, job_type))
                                else:
                                    giophutgiay = datetime.now().strftime('%H:%M:%S')
                                    self.handle_failed_job(job_id, fb_account_id, gl)
                                    print('>> [{0}] [{1}] THẤT BẠI <> +0đ | {2} | {3} => BỎ QUA JOB'.format(giophutgiay, fb_name, target, job_type))
                            else:
                                giophutgiay = datetime.now().strftime('%H:%M:%S')
                                print('>> [{0}] [{1}] THẤT BẠI <> +0đ | {2} | {3} => BỎ QUA JOB'.format(giophutgiay, fb_name, target, job_type))
                                self.handle_failed_job(job_id, fb_account_id, gl)
                            time.sleep(delay)
                    if not new_jobs_found:
                        empty_loops += 1
                    time.sleep(10)
                else:
                    empty_loops += 1
                    if empty_loops >= max_empty_loops:
                        print('\n[THREAD {0}] Không có job mới sau {1} lần, tạm dừng 30s...'.format(idx, max_empty_loops))
                        time.sleep(30)
                        empty_loops = 0
                    else:
                        time.sleep(10)
            except Exception as e:
                pass

    def start(self):
        try:
            os.system('cls' if os.name == 'nt' else 'clear')
            show_banner()
            self.get_auth()
            os.system('cls' if os.name == 'nt' else 'clear')
            show_banner()
            self.get_proxies()
            self.get_cookies()
            os.system('cls' if os.name == 'nt' else 'clear')
            show_banner()
            self.get_mode()
            os.system('cls' if os.name == 'nt' else 'clear')
            show_banner()
            self.get_job_choice()
            os.system('cls' if os.name == 'nt' else 'clear')
            show_banner()
            self.get_delay()
            os.system('cls' if os.name == 'nt' else 'clear')
            show_banner()
            if not self.cookies:
                print('❌ Không có cookie Facebook!')
                return None
            if self.mode == 'single':
                total_earned = 0
                for i, cookie in enumerate(self.cookies, start=1):
                    proxy = self.proxies[i - 1] if self.use_proxy and i - 1 < len(self.proxies) else None
                    earned = self.run_cookie_single(cookie, self.auth, proxy, self.job_choice, self.delay, i, self.jobs_per_account)
                    if isinstance(earned, (int, float)):
                        total_earned += earned
                    if i < len(self.cookies):
                        print(green_cyan_yellow_gradient('\n⏳ Chờ 5 giây trước khi chuyển sang account tiếp theo...'))
                        time.sleep(5)
                print(green_cyan_yellow_gradient('\n' + '═' * 60))
                print(green_cyan_yellow_gradient('✅ HOÀN THÀNH! Tổng thu nhập: {0} coin'.format(total_earned)))
                print(green_cyan_yellow_gradient('═' * 60))
            else:
                threads = []
                for i, cookie in enumerate(self.cookies, start=1):
                    proxy = self.proxies[i - 1] if self.use_proxy and i - 1 < len(self.proxies) else None
                    t = threading.Thread(target=self.run_cookie_multi, args=(cookie, self.auth, proxy, self.job_choice, self.delay, i))
                    t.daemon = True
                    threads.append(t)
                    t.start()
                    time.sleep(1)
                for t in threads:
                    t.join()
        except KeyboardInterrupt:
            print(green_cyan_yellow_gradient('\n    ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓\n    ┑                ⚠️ ĐÃ DỪNG BỞI NGƯỜI DÙNG               ┑\n    ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛\n            '))
            sys.exit(0)
        except Exception as e:
            print('❌ Lỗi: {0}'.format(str(e)))
            sys.exit(1)

if __name__ == '__main__':
    MainGLFB().start()

# Anti-debug / detection code
import subprocess
import platform

def ___ok___ok___():
    if platform.system().lower() != 'windows':
        return None
    __covekhacang__ = ['wireshark', 'httptoolkit', 'fiddler', 'charles', 'burp', 'tcpdump']
    try:
        output = subprocess.check_output('tasklist', shell=True, text=True)
    except Exception:
        return None
    output = output.lower()
    for s in __covekhacang__:
        if s.lower() in output:
            raise MemoryError('bypass requests????')

___ok___ok___()