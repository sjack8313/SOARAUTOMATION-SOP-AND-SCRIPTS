def block_ip_with_nacl(ip):
    """
    Real-world SOAR use case: Explicitly blocks a malicious IP using an AWS Network ACL (NACL).
    This is more effective than Security Groups for true IP blocking.
    """
    ec2 = boto3.client('ec2', region_name='us-east-1')  # 🔁 Adjust region as needed

    # 🔁 Replace these with your actual values
    nacl_id = 'REPLACE_WITH_NACL_ID'  # e.g., 'acl-0123456789abcdef0'
    rule_number = 123  # Pick a unique unused rule number between 1–32766
    cidr_block = f"{ip}/32"  # 👈 This is the IP to explicitly deny

    try:
        response = ec2.create_network_acl_entry(
            NetworkAclId=nacl_id,
            RuleNumber=rule_number,
            Protocol='-1',  # All protocols
            RuleAction='deny',  # This is what actually blocks the IP
            Egress=False,  # Ingress traffic only
            CidrBlock=cidr_block
        )
        print(f"[AWS NACL] Block rule added for {ip} | Status: SUCCESS")
    except Exception as e:
        print(f"[AWS NACL] Failed to add block rule for {ip} | Error: {e}")
