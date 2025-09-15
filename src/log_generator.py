import random
import datetime

def generate_logs(n_rows: int, output_path: str = "data/synthetic_logs.log"):
    ips = ["192.168.1.1", "10.0.0.5", "172.16.0.22", "8.8.8.8", "123.45.67.89"]
    urls = ["/", "/home", "/about", "/login", "/products", "/contact"]
    status_codes = [200, 200, 200, 404, 500, 302]
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
        "curl/7.68.0",
        "Googlebot/2.1 (+http://www.google.com/bot.html)"
    ]

    with open(output_path, "w") as f:
        for _ in range(n_rows):
            ip = random.choice(ips)
            timestamp = datetime.datetime.now() - datetime.timedelta(seconds=random.randint(0, 100000))
            url = random.choice(urls)
            code = random.choice(status_codes)
            ua = random.choice(user_agents)
            line = f'{ip} - - [{timestamp.strftime("%d/%b/%Y:%H:%M:%S")} +0000] "GET {url} HTTP/1.1" {code} {random.randint(200,5000)} "{ua}"\n'
            f.write(line)

    print(f"✅ Generated {n_rows} logs in {output_path}")
