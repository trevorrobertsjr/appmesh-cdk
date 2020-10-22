#!/usr/bin/env python3

from aws_cdk import core

from appmesh_cdk.appmesh_cdk_stack import AppmeshCdkStack


app = core.App()
AppmeshCdkStack(app, "appmesh-cdk")

app.synth()
