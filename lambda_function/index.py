import json

def lambda_handler(event, context):
    print('イベントを受信しました:', event)
    
    return {
        'statusCode': 200,
        'body': json.dumps('Lambda関数が正常に実行されました！')
    } 