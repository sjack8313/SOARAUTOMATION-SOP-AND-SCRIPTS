**STANDARD OPERATING PROCEDURE (SOP)**

**Title:** Deploying and Automating Splunk SOAR Playbooks for Incident Response

---

### **Objective:**

To define a repeatable, standardized procedure for developing, uploading, triggering, and deploying Splunk SOAR playbooks that execute automated response actions such as blocking IPs via AWS, firewalls (e.g., Barracuda, Palo Alto), or other integrated devices.

---

### **Tools Required:**

* Splunk SOAR (Cloud or On-Prem)
* Splunk Enterprise or Enterprise Security (for correlation alerts)
* API keys or credentials for integrated tools (AWS, Barracuda, Palo Alto, etc.)
* Python knowledge for playbook scripting
* Admin-level access to Splunk and SOAR platforms

---

### **Sections:**

1. Setting Up Splunk SOAR
2. Creating a SOAR Playbook
3. Writing Python Automation Scripts
4. Uploading and Wiring Playbooks
5. Triggering Playbooks via Splunk Alerts
6. API Integration Examples
7. GitHub Usage and Documentation Format

---

### **1. Setting Up Splunk SOAR**

1. Install or access SOAR:

   * Cloud URL (e.g., `https://soar.company.com`)
   * On-premise instance via admin portal
2. Ensure asset configuration:

   * Go to **Administration > Asset Settings**
   * Add assets for AWS, firewalls, EDR, etc.
   * Test connectivity with valid credentials

---

### **2. Creating a SOAR Playbook**

1. Navigate to **Automation > Playbooks**
2. Click **"Create Playbook"**
3. Choose method:

   * **Visual Editor**: drag-and-drop logic
   * **Python Editor**: full code control
4. Name and tag your playbook appropriately (e.g., `Block_Malicious_IP`)

---

### **3. Writing Python Automation Scripts**

Use Python within SOAR to create playbooks with Phantom SDK functions.

#### Example: Blocking IP on Barracuda

```python
def block_ip(container):
    ip = container.get('source_address')
    phantom.act("block ip", parameters=[{"ip": ip}], asset="barracuda_fw")
```

#### Example: Blocking IP on AWS Security Group

```python
import boto3

def block_ip_aws(container):
    ip = container.get('source_address')
    ec2 = boto3.client('ec2', aws_access_key_id='...', aws_secret_access_key='...')
    ec2.revoke_security_group_ingress(GroupId='sg-xxxxxx', CidrIp=ip + "/32", IpProtocol="-1")
```

---

### **4. Uploading and Wiring Playbooks**

**Option 1: Visual Editor**

* Add custom function block
* Create and paste script
* Connect to upstream/downstream logic blocks (e.g., threat intelligence, decision blocks)

**Option 2: Python Editor**

* Define `on_start`, `block_ip`, `decision_1`, etc.
* Call `phantom.act()` or `phantom.debug()` as needed
* Save and validate syntax

---

### **5. Triggering Playbooks via Splunk Alerts**

1. Go to Splunk ES > **Configure > Content Management > Correlation Searches**
2. Edit or create a rule (e.g., `Brute Force Detection`)
3. Under **Actions**, select `Send to SOAR`
4. Match alert tags with playbook trigger tags
5. Pass required fields such as IP, host, geo, timestamp

---

### **6. API Integration Examples**

| Device/API  | Integration Method      | Notes                              |
| ----------- | ----------------------- | ---------------------------------- |
| AWS         | boto3 + IAM credentials | Block via Security Groups or WAF   |
| Barracuda   | REST API                | Requires API key & endpoint        |
| Palo Alto   | XML API                 | Use URL filtering or IP block list |
| CrowdStrike | REST API                | Use detection ID to contain host   |

---

# Paste actual playbook script here
````

## Output

* IP blocked in Barracuda and AWS SG
* Analyst notified via Slack and Splunk alert

```

---

### ✅ SOP Checklist Summary
- [ ] Access SOAR and configure assets
- [ ] Write or upload Python playbook
- [ ] Create correlation rule in Splunk
- [ ] Match trigger conditions (e.g., tag, severity)
- [ ] Test playbook and validate API actions
- [ ] Document and commit to GitHub

```
