import json, requests, os

atoken = os.environ['ACCESS_TOKEN']

def postToLine(atoken, token, text):
    url = 'https://api.line.me/v2/bot/message/reply'
    headers = {'Authorization': 'Bearer ' + atoken}
    data = {
        "replyToken": token,
        "messages":[{
            "type":"text",
            "text": text 
        }]
    }

    return (requests.post(url, headers=headers, json=data).json())
    


def lambda_handler(event, context):
    token = json.loads(event["body"])["events"][0]["replyToken"]
    message = postToLine(atoken, token, "xxxxxx")
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": message,
        }),
    }