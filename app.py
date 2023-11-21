#!/usr/bin/env python3
import os

import aws_cdk as cdk
from aws_cdk import Tags

from kinesis_stream.kinesis_stream_stack import KinesisStreamStack
from data_producer.data_producer_stack import DataProducerStack
from data_consumer.data_consumer_stack import DataConsumerStack
from s3_bucket.s3_bucket_stack import S3BucketStack

env_USA = cdk.Environment(account="", region="us-west-2")
app = cdk.App()

kinesis_stream = KinesisStreamStack(app, "KinesisStreamStack", env=env_USA)
data_producer = DataProducerStack(app, "DataProducerStack", env=env_USA)
data_consumer = DataConsumerStack(app, "DataConsumerStack", env=env_USA)
s3_bucket = S3BucketStack(app, "S3BucketStack", env=env_USA)

Tags.of(app).add("ProjectOwner", "Alex-Clark")
Tags.of(app).add("ProjectName", "Crypto_incremental-Pipeline")

app.synth()
