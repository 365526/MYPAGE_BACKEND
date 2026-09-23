import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = os.getenv("ALLOWED_ORIGINS", "http://localhost:5173").split(",")
app.add_middleware(CORSMiddleware, allow_origins=origins,
                   allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

PROFILE = {
    "name": "김소희",
    "role": "석사과정 · 정보영재트랙",
    "intro": "파견연구교사로\n2학기 재학 중입니다.",
    "interests": {
        "role": "AI 융합 교육",
        "items": ["인공지능과 교육", "교육 데이터 분석", "교육용 SW 개발"],
    },
    "project": {
        "role": "AI 기반 개발 실습",
        "desc": "관광 공공데이터를 활용한",
        "highlight": "여행 계획 프로그램 개발",
    },
    "goal": {
        "role": "연구 준비",
        "desc": "선행연구 분석을 통한",
        "highlight": "논문 주제 구체화",
    },
}

@app.get("/")
def root():
    return {"message": "자기소개 API입니다. /docs 에서 확인하세요."}

@app.get("/profile")
def get_profile():
    return PROFILE