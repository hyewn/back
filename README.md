# 자기소개 페이지 & 방명록 (Back-End)

### 🖥️ 소개(현재는 서버 종료)
이 FastAPI 서버는 '방명록 기능의 백엔드 역할'을 수행하며, 프론트엔드와 연동되어 작성된 글을 저장하고 보여줍니다. 서버 종료 시 데이터는 유지되지 않습니다.

### 📌 주요 API
- `GET /guestbook` : 방명록 전체 조회
- `POST /guestbook` : 새로운 방명록 작성 (작성자, 내용)
- `DELETE /guestbook/{id}` : 방명록 삭제 (선택 구현 시)

### 🐳 선택 구현(구현함)
- ✅ 누구나 삭제할 수 있는 방명록 삭제 기능
- ✅ Docker를 활용한 FastAPI 배포

### 🔧 기술 스택
- Python 3.10+
- FastAPI
- uvicorn
- (optional) Docker

### 🔗 연동된 Front-End
https://github.com/hyewn/front

