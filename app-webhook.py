from flask import Flask, request, jsonify
import json
import os
import uuid
import requests
from datetime import datetime

app = Flask(__name__)

# 외부 메신저 API 주소
EXTERNAL_MESSENGER_API = "http://xxx.xxx.xxx.xxx/api"

@app.route('/webhook', methods=['POST'])
def webhook():
    # json payload 수신
    alert_json = request.json 

    # 메세지 가공
    alerts = alert_json.get('alerts', [])
    messages = []
    title = []
  
    for alert in alerts:
        labels = alert.get('labels', {})
        annotations = alert.get('annotations', {})
        #msg = f"Alert" {labels.get('alertname')} - {annotations.get('summary', '')}"
        msg = f"NAMESPACE: {labels.get('namespace')} \nPod: {labels.get('pod')} \nStatus: {labels.get('reason')}"
        title = f"NAMESPACE: {labels.get('namespace')} > Status: {labels.get('alertname')}"
        messages.append(msg)
        titles.appen(title)
    message_text = "\n".join(messages)
    title_text = "\n".join(titles)

    # 송신결과 출력
    print(messages_text)

    # x-www-form-urlencoded 형식으로 메세지 생성
    form_data = {
      "SRV_CODE" : BSRD03",
      "SEND": "xxxxxx",
      "TITLE": title_text,
      "BODY": message_text,
      "SENDER_ALIAS": "Alertmanager"
    }

    # message 전송
    response = requests.post(
      EXTERNAL_MESSENGER_API,
      data = form_data,
      headers={"Content-Type": "application/x-www-form-urlencoded"}
    )

    return f"Sent message with status {response.status_code}"
  
@app.route('/')
def hello():
    return "You should call /webhook"

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')
