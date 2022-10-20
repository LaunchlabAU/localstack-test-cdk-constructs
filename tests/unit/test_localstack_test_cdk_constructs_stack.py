import aws_cdk as core
import aws_cdk.assertions as assertions

from localstack_test_cdk_constructs.localstack_test_cdk_constructs_stack import LocalstackTestCdkConstructsStack

# example tests. To run these tests, uncomment this file along with the example
# resource in localstack_test_cdk_constructs/localstack_test_cdk_constructs_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = LocalstackTestCdkConstructsStack(app, "localstack-test-cdk-constructs")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
