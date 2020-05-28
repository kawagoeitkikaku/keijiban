import boto3
import json
from datetime import datetime
import base64

dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):
    # STEP010
    # �t�����g�G���h�������烊�N�G�X�g�p�����[�^���擾����
    # ��L����QA_HEAD_TBL���R�[�h�̍��ڒl���쐬����
    body = json.loads(event['body'])
    POST_NAME = body['POST_NAME']
    POST_MESSAGE = body['POST_MESSAGE']
    USER_ID = 'SYSTEM'
    NOW_DATETIME = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # STEP020
    # KEIJIBAN_SEQ_TBL�̃V�[�P���X�����X�V�E�擾����
    seqtable = dynamodb.Table('KEIJIBAN_SEQ_TBL')
    response = seqtable.update_item(
        Key={ 'TABLE_NAME' : 'KEIJIBAN_TBL' },
        UpdateExpression='set SEQ = SEQ + :val , UDT_USERID = :UDT_USERID , UDT_TIMESTAMP = :UDT_TIMESTAMP',
        ExpressionAttributeValues= { 
           ':val' : 1 ,
           ':UDT_USERID' : USER_ID,
           ':UDT_TIMESTAMP' : NOW_DATETIME
       }, 
       ReturnValues='UPDATED_NEW'
    ) 
    nextval = response['Attributes']['SEQ']

    # STEP030
    # KEIJIBAN_TBL���R�[�h��o�^����
    KEIJIBAN_TBL = dynamodb.Table('KEIJIBAN_TBL')
    KEIJIBAN_TBL.put_item(
        Item = {
            # �Ɩ��Ǘ�����
            'POST_ID' : nextval,
            'POST_NAME' : POST_NAME,
            'POST_MESSAGE' : POST_MESSAGE,
            # �V�X�e���Ǘ����� 
            'CRT_USERID' : USER_ID,
            'CRT_TIMESTAMP' : NOW_DATETIME,
            'UDT_USERID' : USER_ID,
            'UDT_TIMESTAMP' : NOW_DATETIME
        }    
    )

    return {
        'statusCode' : 200,
        'headers' : {
            'access-control-allow-origin' : '*',
            'content-type' : 'application/json'
        },
        'body' : json.dumps({'result' : 1})
    }