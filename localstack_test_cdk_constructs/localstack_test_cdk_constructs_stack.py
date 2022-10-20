from aws_cdk import Stack
from aws_cdk import aws_dynamodb as dynamodb
from aws_cdk import aws_lambda as lambda_
from aws_cdk import aws_lambda_python_alpha as lambda_python
from constructs import Construct


class LocalstackTestCdkConstructsStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        lambda_created_before = lambda_python.PythonFunction(
            self,
            "Before",
            runtime=lambda_.Runtime.PYTHON_3_8,
            entry="functions/python_lambda",
        )

        table = dynamodb.Table(
            self,
            "Table",
            partition_key=dynamodb.Attribute(
                name="keyName", type=dynamodb.AttributeType.STRING
            ),
        )

        lambda_created_after = lambda_python.PythonFunction(
            self,
            "After",
            runtime=lambda_.Runtime.PYTHON_3_8,
            entry="functions/python_lambda",
        )

        # This works
        table.grant_read_data(lambda_created_after)

        # This doesn't work.
        table.grant_read_data(lambda_created_before)
