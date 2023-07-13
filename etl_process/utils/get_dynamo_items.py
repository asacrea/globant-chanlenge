import boto3

def lambda_handler(event, context):
    
    bucket_name = event['bucket_name']
    key_name = event['key_name']
    source_file_name = event['file_name']
    file_name = source_file_name.split('/')[-1]

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('etl_config')  # Replace with your actual DynamoDB table name

    # Specify the key of the item you want to retrieve
    item_key = {
        'file': 'hired_employees'
        # Add more key-value pairs as needed for composite primary keys
    }
    
    # Retrieve the item from DynamoDB
    response = table.get_item(Key=item_key)['Item']
    
    
    return {
        'parameters':
        {
            'itemList': response,
            'bucket_name': bucket_name,
            'key_name': key_name,
            "load_path": "s3://globant-bucket-2/stage/",
            'source_file_name': source_file_name
        }
    }
