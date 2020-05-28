import boto3
  
dynamodb = boto3.resource('dynamodb')
table    = dynamodb.Table('KEIJIBAN_TBL')
  
def get_cns_profile():
    response = table.scan()
    return response['Items']
    
def lambda_handler(event, context):
    return get_cns_profile()