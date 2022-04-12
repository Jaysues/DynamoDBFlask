import boto3

dynamo_client = boto3.client('dynamodb')

def get_items():
    response = dynamo_client.scan(
        TableName='YourTestTable'
    )

    data = [
        {
            "userName": item.get("userName").get("S"),
            "officeLabel": item.get("officeLabel").get("S"),
            "createdAt": item.get("createdAt").get("S"),
            "numDesks": item.get("numDesks").get("S")
        } for item in response.get("Items")
    ]
    return data

def put_item(userName, officeLabel, createdAt, numDesks):
    return dynamo_client.put_item(
        TableName='YourTestTable',
        Item={
            "userName": {
              "S": userName
            },
            "officeLabel": {
              "S": officeLabel
            },
            "createdAt": {
              "S": createdAt
            },
            "numDesks": {
              "S": numDesks
            }
        }   
    )
