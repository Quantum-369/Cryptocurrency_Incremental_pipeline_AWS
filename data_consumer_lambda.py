import os
import boto3
import json
import base64
from decimal import Decimal

TABLE_NAME = os.environ["DYNAMO_TABLE_NAME"]


def handler(event, context):
    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.Table(TABLE_NAME)

    for record in event["Records"]:
        payload = base64.b64decode(record["kinesis"]["data"])
        data = json.loads(payload.decode("utf-8"), parse_float=Decimal)
        data["ticker"] = data["from_currency_code"] + data["to_currency_code"]
        table.put_item(Item=data)
