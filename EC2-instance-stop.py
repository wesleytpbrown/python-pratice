import boto3

ec2 = boto3.client('ec2')


def stop_running_instances():
    #describe all instances in running state
    response = ec2.describe_instances(
        Filters=[
            {'Name':'instance-state-name', 'Values':['running']}
        ]
    )


    #extract instance ID's
    running_instances = [instance['InstanceID']
        for reservation in response['Reservstions']
        for instance in reservation['Instances']]
    
    if running_instances:
        print ('Stopping Instances: ', running_instances )
        ec2.stop_instances(InstanceIDs=running_instances)
        print ('Stop request sent.')
    else:
        print ('No running instances found.')

#Run the function
stop_running_instances()