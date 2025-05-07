def block_malicious_sender(email):
    """
    Simulates blocking a phishing sender in Microsoft 365 using Graph API.
    Used in our Security workflows to prevent repeat phishing attempts.
    """
    graph_api_url = "https://graph.microsoft.com/v1.0/security/tiIndicators"  # 🔁 Replace with Graph API endpoint if different
    graph_headers = {
        "Authorization": "Bearer REPLACE_WITH_GRAPH_API_TOKEN",  # 🔁 Replace with your MS Graph API OAuth token
        "Content-Type": "application/json"
    }
    graph_payload = {
        "indicatorType": "email",
        "indicatorValue": email,  # 👈 Email address to block
        "action": "block",
        "description": "SOAR Automation: Blocked phishing sender",
        "expirationDateTime": "2025-12-31T23:59:59Z"
    }
    graph_response = requests.post(graph_api_url, headers=graph_headers, json=graph_payload)
    print(f"[O365] Blocked sender {email} | Status: {graph_response.status_code}")
