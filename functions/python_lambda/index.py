
from aws_lambda_powertools import Logger, Tracer
from aws_lambda_powertools.utilities.data_classes import (
    DynamoDBStreamEvent,
    event_source,
)
from aws_lambda_powertools.utilities.typing import LambdaContext




tracer = Tracer()
logger = Logger()


@logger.inject_lambda_context()
@tracer.capture_lambda_handler
@event_source(data_class=DynamoDBStreamEvent)
def handler(event: DynamoDBStreamEvent, context: LambdaContext):
    pass