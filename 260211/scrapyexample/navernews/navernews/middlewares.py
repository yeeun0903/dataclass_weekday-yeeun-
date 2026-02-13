# 인스타그램 사이트 크롤링 : 최초의 값을 가져올 때, 실수 -> 피곤해짐
# 완성되지 않은 상태에서 크롤링 -> 브라우저 & ip 차단됨
# 미들웨어 : 가상브라우저 A -> 가상브라우저 B
# 주언어 한글 -> 영어로

import random

class RandomUserAgentMiddleware :
    USER_AGENTS = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36",
    ]

    def process_request(self, request, spider) :
        request.headers.setdefault("Accept-Language", "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7")
        request.headers["User-Agent"] = random.choice(self.USER_AGENTS).encode("utf-8")
        return None     