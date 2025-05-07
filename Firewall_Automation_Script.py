def block_ip_barracuda(ip):
    """
    Standalone SOAR playbook to block an IP on Barracuda firewall.
    Used by MSSPs, hybrid SOCs, or enterprise IR teams.
    """
    url = "https://barracuda-fw.local/api/block"  # 🔁 Replace with your actual Barracuda firewall API URL or any other Firewall API that is needed
    headers = {
        "Authorization": "Bearer REPLACE_WITH_BARRACUDA_API_KEY",  # 🔁 Replace with your Barracuda API token or other firewall I just use barraccuda here
        "Content-Type": "application/json"
    }
    payload = {"ip": ip}  # 👈 IP to block is passed here
    response = requests.post(url, headers=headers, json=payload)
    print(f"[Barracuda] IP {ip} blocked | Status: {response.status_code}")
