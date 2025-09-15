# webhook-store
python 애플리케이션을 이용해 Alert(JSON)을 로컬에 저장하는 테스트

## Installation
1) 애플리케이션 프로젝트 생성
```
$ oc new-project webhook-store
```
2) 애플리케이션 생성
```
oc new-app --name=webhook-store --labels="application=webhook-store-app"  python:3.9-ubi9~https://github.com/alezzandro/webhook-store 
```
3) Service 생성
```
oc expose service webhook-store -l application=webhook-store-app --name=webhook-store
```

4) 결과
/tmp/webhook 디렉토리에서 alert 데이터 저장

# webhook alert
저장된 alert(json)데이터를 가공하여, 외부 메신저로 전송하는 애플리케이션
외부 메신저 규격에 맞춰 header로 전달
