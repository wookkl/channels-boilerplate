# channels-boilerplate

## Project setting check list
- [x] Settings check list
    - [x] 장고 기본적인 로컬, 개발, 프로덕션 환경 세팅
    - [x] ASGI_APPLICATION
    - [x] DATA_UPLOAD_MAX_MEMORY_SIZE
    - [x] CHANNEL_LAYERS
    - [x] S3 사용할 경우
        - [x] AWS_REGION
        - [x] AWS_STORAGE_BUCKET_NAME
        - [x] AWS_S3_CUSTOM_DOMAIN
        - [x] AWS_ACCESS_KEY_ID
        - [x] AWS_SECRET_ACCESS_KEY
        - [x] AWS_DEFAULT_ACL
    - [x] SWAGGER_SETTINGS
- [x] routing.py 생성해서 asgi application 생성
- [x] asgi.py에 application 변경 
- [x] url.py에 swagger url 추가
    
## Chat app
- [x] routing.py 에 websocket urlpatterns을 생성해서 라우팅
- [x] 모든 Consumer에 들어오는 received content들은 해당 Consumer의 핸들러로 넘겨서 처리
- [x] content에 포함되어 있는 event에 따라 핸들어의 on 메서드가 실행 

## Core app
- [x] 타임 스탬프 추상 모델 생성
- [x] JWT 인증을 위한 미들웨어 생성