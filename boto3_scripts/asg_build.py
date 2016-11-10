#!/usr/bin/env python
'''
demo script to show how to create an ASG of servers behind a ELB
'''

import boto3

# important note: I did not build an elb into the creation script, you need to
# pre-create the elb and place its name in the elb_name variable to make this work

# various variables to define server stack being created
# need ImageId, MinCount, MaxCount, InstanceType, vpcId, etc
region = 'us-west-1'
network_vpc = 'vpc-23ba6646'
image_id = 'ami-823461e2'
sec_group = ['sg-d44556b0']
instance_type = 't2.micro'
key_name = 'home'
elb_name = ['demotest']
subnet = 'subnet-380ab85d'
mins = 3
maxs = 3

client = boto3.client('autoscaling', region_name=region)

# create autoscaling launch configuration template
client.create_launch_configuration(LaunchConfigurationName='testlaunch',
                                   ImageId=image_id,
                                   KeyName=key_name,
                                   SecurityGroups=sec_group,
                                   InstanceType=instance_type)

# create an autoscaling group using the pre-defined launch configuration
client.create_auto_scaling_group(AutoScalingGroupName='test1',
                                 MinSize=mins,
                                 MaxSize=maxs,
                                 LoadBalancerNames=elb_name,
                                 LaunchConfigurationName='testlaunch',
                                 VPCZoneIdentifier=subnet)
