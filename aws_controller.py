import boto3

dynamo_client = boto3.client('dynamodb')

def get_items():
    return dynamo_client.scan(
        TableName='BaseDeArtistas'
    )

def put_movie(artist, uuid, plot, rating, dynamodb=None):
    table = dynamodb.Table('BaseDeArtistas')
    response = table.put_item(
       Item={
            'Artista': artist,
            'UUID': uuid,
        }
    )
    return response