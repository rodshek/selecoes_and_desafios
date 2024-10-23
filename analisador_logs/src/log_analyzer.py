import re
from collections import Counter, defaultdict

from utils import read_log_file


def analyze_logs(log_file_path):
    # Expressão regular para capturar o IP, status HTTP, e a hora da requisição
    log_pattern = r'(?P<ip>\d{1,3}(?:\.\d{1,3}){3}) - - \[(?P<time>[^\]]+)\] "(?:GET|POST) [^"]+" (?P<status>\d{3})'

    logs = read_log_file(log_file_path)

    ips = Counter()
    statuses = Counter()
    requests_per_hour = defaultdict(int)

    for log in logs:
        match = re.match(log_pattern, log)
        if match:
            ip = match.group('ip')
            status = match.group('status')
            time = match.group('time')
            hour = time.split(':')[1]  # Extrai a hora da requisição

            ips[ip] += 1
            statuses[status] += 1
            requests_per_hour[hour] += 1

    return {
        'ips': ips,
        'statuses': statuses,
        'requests_per_hour': requests_per_hour
    }
