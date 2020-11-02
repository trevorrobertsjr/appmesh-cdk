from aws_cdk import core
from aws_cdk.core import Duration
import aws_cdk.aws_ec2 as ec2
import aws_cdk.aws_eks as eks
import aws_cdk.aws_iam as iam
import aws_cdk.aws_sqs as sqs

class AppmeshCdkStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # The code that defines your stack goes here
        queue = sqs.Queue(
            self, "MyFirstQueue",
            visibility_timeout=Duration.seconds(300),
        )
        # serviceaccount = eks.ServiceAccount(self, "appmesh-sa",training-eks-PvBU7905,name="appmesh-sa",namespace="appmesh-system")
        # serviceaccount.add_to_principal_policy(iam.PolicyStatement(
        #     effect=iam.Effect.DENY,
        #     resources=[bucket.bucket_arn, other_role.role_arn],
        #     actions=["ec2:SomeAction", "s3:AnotherAction"],
        #     conditions={"StringEquals": {
        #         "ec2:AuthorizedService": "codebuild.amazonaws.com"}}
        # ))
