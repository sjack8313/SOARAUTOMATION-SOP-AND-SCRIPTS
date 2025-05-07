def block_ip_aws(ip):
    """
    Adds a deny rule to block a malicious IP in an AWS Security Group.
    This is commonly used in cloud-first SOC environments.
    """
    ec2 = boto3.client('ec2', region_name='us-east-1')  # 🔁 Adjust region as needed
    response = ec2.authorize_security_group_ingress(
        GroupId='REPLACE_WITH_YOUR_SG_ID',  # 🔁 Replace with your actual AWS Security Group ID
        IpProtocol='-1',  # Block all protocols
        CidrIp=f"{ip}/32",  # 👈 IP is added here in CIDR format
        FromPort=-1,
        ToPort=-1,
        Description='Blocked by SOAR automation'
    )
    print(f"[AWS] IP {ip} blocked in security group | Status: {response['ResponseMetadata']['HTTPStatusCode']}")
