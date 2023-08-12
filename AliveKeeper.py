import requests
import time


class AliveKeeper:
    def __init__(self, ping_url: str) -> None:
        self.url = ping_url
    
    def keep_alive(self, ping_delay: int):
        heds = {
            'Authority': 'githook.codimcocos.repl.co',
            'Method': 'GET',
            'Path': '/',
            'Scheme': 'https',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 OPR/100.0.0.0 (Edition Yx GX)',
        }
        while True:
            r = requests.get(url=self.url, headers=heds)
            print(f'AliveKeeper requests, response: {r}')
            time.sleep(ping_delay)