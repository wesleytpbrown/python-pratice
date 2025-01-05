
import boto3
#create the client
ec2 = boto3.client('ec2',  region_name='us-east-1')

#define the function with the parameters to start instances
def create_new_instances ():
    instances = ec2.run_instances(
        ImageId='ami-063d43db0594b521b',  
        InstanceType='t2.micro',  
        MinCount=3,
        MaxCount=3,
        KeyName='new-instance-key', 
        SecurityGroupIds=['sg-03b9e4e3fec2e77a7'],  
        SubnetId='subnet-02f8d8e5cfbbd3677'  
    )

    for instance in instances['Instances']:
        print(f"Instance created with the ID: {instance['InstanceId']}")

if __name__ == '__main__':
    create_new_instances()