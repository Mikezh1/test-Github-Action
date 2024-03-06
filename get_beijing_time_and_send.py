# get Beijing time and send
import requests
import json
from datetime import datetime, timedelta
import pytz  # 导入 pytz 模块

def get_beijing_time():
    # Get the current UTC time
    utc_now = datetime.utcnow()
    
    # Set the timezone for Beijing
    beijing_tz = pytz.timezone('Asia/Shanghai')
    
    # Convert UTC time to Beijing time
    beijing_now = utc_now + timedelta(hours=8)  # Beijing is 8 hours ahead of UTC time
    beijing_now = beijing_tz.localize(beijing_now)
    
    return beijing_now

def send_Feishu_message(text, include_timestamp=True):
    if include_timestamp:
        current_time = current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        text = text + f"\n----------------------\nMessage Sent Time: {current_time}"
    
    url = "https://open.feishu.cn/open-apis/bot/v2/hook/ed0b78fa-0e14-47cf-b190-e56419356b8d"
    
    payload = json.dumps({
        "msg_type": "text",
        "content": {
            "text": text
        }
    })
    
    headers = {
        'Content-Type': 'application/json'
    }
    
    response = requests.post(url, headers=headers, data=payload)
    
    return response.text

if __name__ == "__main__":

    beijing_time = get_beijing_time().strftime("%Y-%m-%d %H:%M:%S")
    
    theme = "New notification"
    
    # Example usage
    message_text = \
    f"""#{theme}#\n
This is a Python automatically sent text message \n\n
Beijing time: {beijing_time}"""
    response = send_Feishu_message(message_text)
    
    print(response)
