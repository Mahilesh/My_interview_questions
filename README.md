Company wise - I will upload the questions & answers

## 📚 Table of Contents

- [MIRAFRA - Bangalore (L1 - virtual)](#mirafra---bangalore-l1---virtual)
- [Eurofins India IT Solutions - Bangalore (L1 - virtual)](#eurofins-india-it-solutions---bangalore-l1---virtual)
- Siemens
- Capgemini (L1 - virtual)]


# Questions
### MIRAFRA - Bangalore (L1 - virtual)

1. Introduce yourself
2. CI/CD Workflow
3. Terraform – How do you manage an existing EC2 instance by using Terraform?
4. Docker – How do you ensure security while writing the Dockerfile?
5. Kubernetes – How do you restrict not creating additional pods?
6. GitLab/GitHub – Restrict creating new branches when already 4 branches exist
7. AWS – Auto Load Balancer troubleshooting steps
8. Linux – Get exact matching word in a file
9. Ansible
10. By using Python - what automation scripts you have created?
11. Which Kubernetes are you currently using - Self-hosted or Cloud Provider like EKS?


# Answers

### MIRAFRA - Bangalore (L1 - Virtual) 

## 1. Introduce yourself
- Share your name, experience (e.g., 3.5+ years as a DevOps Engineer), key skills (CI/CD, AWS, Docker, Kubernetes, Terraform, Python scripting), and notable projects or achievements.

## 2. CI/CD Workflow
- Explain your CI/CD pipeline: Code commit → Build (Maven/Gradle) → Test (Unit/Integration) → Static Code Scan (SonarQube) → Artifact Repository (Nexus) → Deployment (Kubernetes/Docker) → Notification (Slack/Email).

## 3. Terraform – How do you manage an existing EC2 instance by using Terraform?
- If **created using Terraform**: Modify the Terraform configuration and apply changes directly.
- If **not created using Terraform**: Use `terraform import` to bring it into the Terraform state, then define its configuration.

## 4. Docker – How do you ensure security while writing the Dockerfile?
- Use minimal base images (like `alpine`)
- Avoid using `latest` tag
- Run containers as non-root
- Scan images using tools like Trivy
- Avoid hardcoding secrets

## 5. Kubernetes – How do you restrict not creating additional pods?
- Set **`replicas`** in the Deployment YAML.
- Use **ResourceQuotas** and **LimitRanges** in the namespace.
- Implement **PodDisruptionBudgets** and **Admission Controllers** for policy enforcement.

## 6. GitLab/GitHub – Restrict creating new branches when already 4 branches exist
- Use **branch protection rules** to allow only certain roles to create new branches.
- Set permissions in GitLab/GitHub to **developer** role (prevent branch creation).
- Use Git hooks or CI pipeline to restrict unauthorized branches.

## 7. AWS – Auto Load Balancer troubleshooting steps
- Check **ALB/NLB logs** in CloudWatch
- Verify **target group health checks**
- Use **VPC Flow Logs** to inspect network traffic
- Validate **security groups**, **route tables**, and **listener rules**
- Use `aws elbv2 describe-*` CLI for status

## 8. Linux – Get exact matching word in a file
```bash
grep -w 'india' mahilesh.txt
```
    
### 9. Ansible  
I have used Ansible for configuration management and automation tasks such as:  
- Installing and configuring software packages on multiple servers  
- Managing system updates and reboots  
- Deploying application code  
- Creating reusable roles for common setups like Docker, Nginx, Java, etc.  
- Using inventory files and `ansible-vault` for managing secrets securely

### 10. By using Python - what automation scripts you have created?  
I have written Python scripts to automate several DevOps tasks, such as:  
- Parsing and monitoring logs for errors or patterns (ELK integration)  
- Automating AWS resource creation via `boto3` (e.g., S3 buckets, EC2 tagging)  
- Scheduled health checks for services and sending alerts  
- Auto-generating configuration files (YAML, JSON) based on templates  
- Git operations automation like cleanup of old branches or triggering pipelines

### 11. Which Kubernetes are you currently using - Self-hosted or Cloud Provider like EKS?  
I am currently using **Amazon EKS (Elastic Kubernetes Service)**, which is a managed Kubernetes service.  
It simplifies cluster management, auto-scaling, and integrates well with other AWS services like IAM, CloudWatch, and ELB.  
In previous projects, I have also worked with self-hosted Kubernetes on virtual machines using kubeadm.

# Questions
### Eurofins India IT Solutions - Bangalore (L1 - virtual)

1. Introduce yourself
2. CI/CD Workflow
3. Static IP vs Dynamic IP
4. Private IP is not visible, we should use only public IP but needs to be restricted. How?
5. Why your org considers Autoscaling instead of Reserved or Spot Instances?
6. Terraform Architecture
7. Difference between main.tf vs terraform.tfstate vs terraform.tfvars
8. GitLab CI/CD - YAML for rollout/rollback deployment
9. What is Terraform State File?
10. Difference Between TCP vs UDP
11. What is TLS?
12. How You Reduced Monthly Costs by 20% Through EC2?
13. How Did You Create Kubernetes Cluster Using Terraform? Was CI/CD Used?
14. DNS is Not Working in Linux – How to Check Connectivity and Troubleshoot
15. Developer somehow saw the secret which is hardcoded. Are you able to modify and make it invisible WITHOUT RESTART? If yes, how?
16. Port 8080 mapped to one instance and 443 to other instances – how do you find which is public and which is private?
17. Error code - 404 - what it means?
18. Write a shell script - which you written recently?
19. Difference between git merge vs git rebase



# Answers

### Eurofins India IT Solutions - Bangalore (L1 - virtual)

## 3. Static IP vs Dynamic IP
- **Static IP**: Manually assigned, doesn’t change over time (e.g., useful for DNS, VPN).
- **Dynamic IP**: Automatically assigned by DHCP and may change periodically.
- ✅ Use static IPs when consistency is important. Useful for whitelisting and DNS mapping.

---

## 4. Private IP is not visible, we should use only public IP but needs to be restricted. How?
- Associate Elastic IP (public) with instance.
- Use Security Groups/NACLs to allow traffic only from whitelisted IPs or CIDRs.
- Use NACLs or AWS WAF for additional filtering.
- Optionally, use VPN or Bastion Host for additional control.

---

## 5. Why your org considers Autoscaling instead of Reserved or Spot Instances?
- **Auto Scaling** provides:
  - Elasticity: Adds/removes instances based on load.
  - Availability: Maintains healthy instance count.
- **Reserved instances** save cost but don’t scale.
- **Spot instances** are cheap but can be interrupted anytime.

✅ So Auto Scaling = balance between cost, scalability, and availability.

---

## 6. Terraform Architecture
**Core components**:
- Terraform CLI  
- Provider plugins (AWS, Azure, etc.)  
- `.tf` files = Configuration  
- State file = Infrastructure snapshot  

**Workflow**: `Write → Plan → Apply → Maintain`

---

## 7. Difference between `main.tf` vs `terraform.tfstate` vs `terraform.tfvars`

| File               | Purpose                                      |
|--------------------|----------------------------------------------|
| `main.tf`          | Main configuration file (resource definitions) |
| `terraform.tfvars` | Variable values (like region, instance type)  |
| `terraform.tfstate`| Stores infrastructure state (actual resource info) |

---

## 9. GitLab CI/CD - YAML for rollout/rollback deployment

```yaml
stages:
  - deploy

deploy_app:
  stage: deploy
  script:
    - echo "Rolling out deployment"
    - kubectl apply -f deployment.yaml

rollback_app:
  stage: deploy
  when: manual
  script:
    - echo "Rolling back deployment"
    - kubectl rollout undo deployment/my-app
```

## 10. What is Terraform State File?

- `.tfstate` file stores the **current state** of your infrastructure.
- Helps Terraform **track resource changes** and **perform diffs**.
- **Do not edit manually**.
- Store in a **remote backend** like AWS S3 (with locking via DynamoDB) for team collaboration and safety.

---

## 11. Difference Between TCP vs UDP

| Feature              | TCP                      | UDP                   |
|----------------------|---------------------------|------------------------|
| Type                 | Connection-based          | Connectionless         |
| Reliability          | Reliable                  | Unreliable             |
| Speed                | Slower (3-way handshake)  | Faster                 |
| Use Case             | HTTP, SSH, FTP            | DNS, VoIP, Streaming   |

---

## 12. What is TLS?

- **TLS (Transport Layer Security)** encrypts data during transmission.
- It **replaces SSL** (Secure Sockets Layer).
- Ensures:
  - **Confidentiality**
  - **Integrity**
  - **Authenticity**
- Commonly used in HTTPS, email, and secure data exchange.

---

## 13. How You Reduced Monthly Costs by 20% Through EC2?

- **Identified underutilized EC2 instances** using CloudWatch metrics.
- **Rightsized instances** from large types (e.g., `m5`) to efficient types (`t3`).
- **Implemented Auto Scaling** to handle load efficiently.
- **Scheduled stop/start** of non-prod instances using **AWS Lambda and CloudWatch Events**.

---

## 14. How Did You Create Kubernetes Cluster Using Terraform? Was CI/CD Used?

✅ **Yes. Here's how:**

- Used **Terraform** to provision **Amazon EKS** via `aws_eks_cluster` and related resources.
- Automated deployment through **GitLab CI/CD pipelines**:
  - Triggered `terraform apply` on merge to `main` or `release` branches.
- Ensured full **Infrastructure as Code** (IaC) with version-controlled K8s cluster setup.

## 15. DNS is Not Working in Linux – How to Check Connectivity and Troubleshoot

```bash
ping 8.8.8.8             # Check internet connectivity (bypasses DNS)
ping google.com          # Check DNS resolution
cat /etc/resolv.conf     # Check DNS configuration file
systemctl restart network
dig google.com           # Advanced DNS lookup
```

### 16. Developer somehow saw the secret which is hardcoded. Are you able to modify and make it invisible WITHOUT RESTART? If yes, how?

- ✅ Yes, **if the app reads secrets dynamically** (e.g., from environment variables or a secret manager).
- Use tools like:
  - AWS Secrets Manager
  - HashiCorp Vault
- You can also:
  - `kubectl edit secret` → base64 encode → update value → **no pod restart** needed if the app supports live secret reload
- Alternatively:
  - Inject via **Kubernetes Volume** or **Environment Variable**


---

### 17. Port 8080 mapped to one instance and 443 to other instances – how do you find which is public and which is private?

#### Option 1: AWS CLI
```bash
aws ec2 describe-instances --query 'Reservations[].Instances[].{IP:PublicIpAddress,Ports:NetworkInterfaces[].PrivateIpAddress}'
```
#### Option 2: Use nmap for port scan
```bash
nmap -p 8080,443 <IP>
```

### 18. Error code - 404 - what it means?

`404 Not Found`  
- The client can reach the server, but the requested resource (URL/path) does not exist on the server.

---

### 19. Write a shell script - which you written recently?

```bash
#!/bin/bash
# Check disk usage and alert if > 80%

THRESHOLD=80
USAGE=$(df -h / | grep -v Filesystem | awk '{print $5}' | sed 's/%//')

if [ "$USAGE" -gt "$THRESHOLD" ]; then
  echo "Disk usage is above $THRESHOLD%, please take action!"
  # Send email/slack alert here
fi
```

### 20. Difference between `git merge` vs `git rebase`

| Feature    | Merge                                 | Rebase                               |
|------------|---------------------------------------|--------------------------------------|
| History    | Keeps full history with merge commits | Rewrites history (linear)            |
| Safe?      | Yes                                   | Can be dangerous (requires force push) |
| Use Case   | For preserving complete history       | For maintaining a clean commit history |

### 21. What is the difference between port 8080 and port 443?

| Feature            | Port 8080                              | Port 443                                   |
|--------------------|----------------------------------------|--------------------------------------------|
| **Type**           | Alternative HTTP port                  | Default HTTPS port                         |
| **Protocol**       | HTTP (HyperText Transfer Protocol)     | HTTPS (HTTP Secure with SSL/TLS)           |
| **Security**       | ❌ Not secure (data sent in plain text) | ✅ Secure (encrypted using TLS/SSL)         |
| **Common Usage**   | Development, testing, proxy servers     | Production websites needing encryption      |
| **Browser Support**| Must specify explicitly (`:8080`)      | Automatically used for `https://` URLs      |
| **Default?**       | ❌ No                                   | ✅ Yes (for HTTPS traffic)                  |

---

### Summary

- **Port 443** is used for **secure HTTPS traffic** (encrypted).
- **Port 8080** is typically used for **non-secure HTTP**, often in testing or development environments.

> Example:
> - http://example.com:8080 → HTTP on port 8080
> - https://example.com → HTTPS on port 443

# Questions

### Capgemini - (L1 - virtual)

1. Can you write a simple Dockerfile to build an image for a basic application?
2. What is the full command to create a Docker container?
3. Once you build an image from your source code, how do you dockerize and run it? (Step-by-step commands)
4. After creating a Docker image, how do you push it to a registry and then use it in Kubernetes?
5. Can you write a shell script that monitors the Tomcat service and sends an email notification if the service fails?
6. Can you explain the Kubernetes architecture as implemented in your project?
7. What are the different types of services available in Kubernetes, and when do you use each?
8. How do you configure persistent volumes and persistent volume claims in Kubernetes?
9. What deployment strategies have you implemented in Kubernetes (e.g., Rolling Update, Blue-Green, Canary)?
10. If a Kubernetes scheduler has issues, how would you troubleshoot it?
11. What recent challenges/issues have you encountered in your Kubernetes clusters, and how did you resolve them?
12. Apart from checking console logs, which tools do you use for monitoring or viewing logs in Kubernetes?
13. Can you walk me through the CI/CD flow you have implemented in your project?
14. Can you explain the Kafka architecture used in your organization?
15. What are the key differences between SonicMQ and Kafka?
16. Can you share some examples of complex AWS cloud infrastructure issues you faced and how you resolved them?
17. Why do you deploy applications both on Docker (standalone) and Kubernetes? What’s the reasoning?
18. Where do you store and manage application secrets in your environment?

# Answers

### Capgemini - (L1 - virtual)

1. Can you write a simple Dockerfile to build an image for a basic application?

FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "app.py"]

2. What is the full command to create a Docker container?

docker run -d --name <container_name> -p <host_port>:<container_port> <image_name>:<tag>
docker run -d --name myapp -p 8080:8080 myapp:1.0

3. What is the full command to create a Docker Image?

docker build -t <image_name>:<tag> -f <Dockerfile_path> <build_context>
docker build -t myapp:1.0 -f Dockerfile .

4. Once you build an image from your source code, how do you dockerize and run it? (Step-by-step commands)

Step1:- docker build -t myapp:1.0 .
Step2:- docker images
Step3:- docker run -d --name myapp -p 8080:8080 myapp:1.0
Step4:- docker logs myapp
Step5:- curl http://localhost:8080

5. After creating a Docker image, how do you push it to a registry and then use it in Kubernetes?

Step 1: Tag the image for registry (e.g., Docker Hub or ECR/GCR/ACR):
docker tag myapp:1.0 <registry_username>/myapp:1.0


Step 2: Login and push:
docker login
docker push <registry_username>/myapp:1.0


Step 3: Create a Kubernetes Deployment using that image (deployment.yaml):

apiVersion: apps/v1
kind: Deployment
metadata:
  name: myapp-deployment
spec:
  replicas: 2
  selector:
    matchLabels:
      app: myapp
  template:
    metadata:
      labels:
        app: myapp
    spec:
      containers:
      - name: myapp
        image: <registry_username>/myapp:1.0
        ports:
        - containerPort: 8080


Step 4: Apply in Kubernetes:
kubectl apply -f deployment.yaml
kubectl get pods


Step 5: Expose the service (NodePort/LoadBalancer/Ingress):
kubectl expose deployment myapp-deployment --type=NodePort --port=8080

