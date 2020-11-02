#!/usr/bin/env python

from aws_cdk import core
from appmesh_cdk.appmesh_cdk_stack import AppmeshCdkStack

app = core.App()

stack=AppmeshCdkStack(app, "appmesh-cdk")

app.synth()
