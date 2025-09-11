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

### 6. Can you write a shell script that monitors the Tomcat service and sends an email notification if the service fails?

```bash
#!/bin/bash
# Check if Tomcat service is running
SERVICE="tomcat"
EMAIL="admin@example.com"

if ! systemctl is-active --quiet $SERVICE; then
  echo "Tomcat service is down!" | mail -s "ALERT: Tomcat Down" $EMAIL
fi
```


### 7. Can you explain the Kubernetes architecture as implemented in your project?

## 1. Cluster Setup
- We run a **multi-node EKS cluster** (AWS managed Kubernetes).  
- The cluster consists of **1 control plane** (managed by AWS) and multiple **worker nodes (EC2 instances)** distributed across availability zones for high availability.  
- Nodes are **tainted and labeled** based on the environment (DEV, TST, PRD) and workload type.  

## 2. Node Configuration & Container Runtime
- Worker nodes run **containerd** as the container runtime.  
- Each node has **kubelet** for managing pods and **kube-proxy** for networking.  
- Nodes are part of an **Auto Scaling Group** for dynamic scaling based on load.  

## 3. Deployment & Workload Management
- Applications run in **Pods**, grouped under **Deployments** for rolling updates and scaling.  
- **DaemonSets** are used for running monitoring and logging agents on all nodes.  
- Stateful workloads (like Kafka, databases) use **StatefulSets** with **Persistent Volumes** for storage.  

## 4. Networking & Service Discovery
- We use **Calico CNI plugin** for pod-to-pod networking and network policies.  
- **Services** (ClusterIP, LoadBalancer) expose applications internally or externally.  
- **Ingress** is managed via **AWS ALB Ingress Controller**.  

## 5. Observability & Management
- Non-production clusters are monitored using **Rancher dashboard** for logs and resource utilization.  
- Production clusters integrate with **CloudWatch + Prometheus + Grafana** for metrics and alerting.  

## 6. Secrets & Configs
- Secrets and config maps are stored in **Kubernetes Secrets / ConfigMaps**, with sensitive production secrets optionally integrated with **AWS Secrets Manager**.  

## 7. CI/CD Integration
- Docker images are built via **GitLab CI/CD**, pushed to **ECR**, and deployed to Kubernetes using **Helm charts**.  
- Deployments follow **Rolling Updates**, with **canary releases** for high-risk services.  

## 8. Security & Governance
- **Role-based access control (RBAC)** is configured for all namespaces.  
- **Pod security policies** and **network policies** enforce compliance for production workloads.  

### 8. What are the different types of services available in Kubernetes, and when do you use each?

| Service Type   | Description                                 | Use Case                                  |
|----------------|---------------------------------------------|------------------------------------------|
| **ClusterIP**  | Default service; accessible only inside the cluster | Internal microservices                    |
| **NodePort**   | Exposes service on each node at a static port | Simple external access for testing       |
| **LoadBalancer** | Creates a cloud load balancer to expose service externally | Production access                        |
| **ExternalName** | Maps service to an external DNS name        | Access external service from inside cluster |

### 9. How do you configure persistent volumes and persistent volume claims in Kubernetes?

### Concepts
- **PersistentVolume (PV):**  
  A cluster-wide resource that provides storage (backed by hostPath, NFS, AWS EBS, etc.).  

- **PersistentVolumeClaim (PVC):**  
  A request by a user for storage with specific size and access mode.  

---

### Example YAML

```yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: mypv
spec:
  capacity:
    storage: 5Gi
  accessModes:
    - ReadWriteOnce
  hostPath:               # For demo; in production use NFS, EBS, EFS, etc.
    path: /mnt/data
---
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: mypvc
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 5Gi
```

### 10. What deployment strategies have you implemented in Kubernetes

### 1. Rolling Update
- **Description:** Gradually replaces existing pods with new version pods.  
- **Details:** Ensures zero downtime by updating a few pods at a time.  
- **Use Case:** Default strategy in Kubernetes; suitable for most production deployments.  

---

### 2. Blue-Green Deployment
- **Description:** Runs two identical environments (Blue = current, Green = new).  
- **Details:** Traffic is switched from Blue to Green once the new version is validated.  
- **Use Case:** Minimizes downtime and allows easy rollback by switching traffic back.  

---

### 3. Canary Deployment
- **Description:** Releases the new version to a small subset of users first.  
- **Details:** Performance and stability are monitored before rolling out to all users.  
- **Use Case:** Useful for testing new features in production with reduced risk.

### 11. If a Kubernetes scheduler has issues, how would you troubleshoot it?  

- **Check scheduler logs:**  
  ```bash
  kubectl logs -n kube-system kube-scheduler-<node>
Check node resources:

bash
Copy code
kubectl describe nodes
Verify taints/tolerations or resource constraints preventing pod scheduling.

Check events for scheduling failures:

bash
Copy code
kubectl get events

### 12. Recent Challenges in Kubernetes and Resolutions

- **Pod not starting due to PVC issues**  
  - Cause: PV/PVC binding mismatch.  
  - Resolution: Verified storage class and corrected PVC bindings.  

- **Pods failing health checks**  
  - Cause: Incorrect readiness/liveness probe configuration.  
  - Resolution: Updated probe paths and thresholds.  

- **Node running out of memory**  
  - Cause: Resource requests/limits not properly defined.  
  - Resolution: Adjusted CPU/Memory requests and limits; scaled nodes if required.  

- **Network issues between pods**  
  - Cause: Misconfigured CNI plugin or policy.  
  - Resolution: Checked CNI logs and used `kubectl exec` to debug connectivity.  

---

### 13. Tools for Monitoring and Logs in Kubernetes

- **Monitoring**
  - Prometheus + Grafana for cluster and application metrics.  
  - Metrics Server (`kubectl top pod` / `kubectl top node`) for real-time resource usage.  

- **Logging**
  - ELK Stack (Elasticsearch, Logstash, Kibana) for centralized log aggregation.  
  - Rancher Dashboard for quick visibility in non-production and production.  

- **Tracing**
  - Jaeger and OpenTelemetry for distributed tracing and debugging microservices.  


### 14. Can you walk me through the CI/CD flow you have implemented in your project?  

### Source Control  
- **Git (GitLab/GitHub)** → triggers pipelines on commit/merge  

### CI Pipeline  
1. **Build Docker image**  
2. **Run unit tests**  
3. **Code linting & SonarQube analysis**  

### CD Pipeline  
1. **Push Docker image** to container registry (ECR/ACR/Harbor)  
2. **Deploy to environments** (Dev → QA → Production) using **Helm charts / Kubernetes manifests**  
3. **Rollback** automatically if errors are detected
 
### 15. Can you explain the Kafka architecture used in your organization?  

- **Broker**: Stores and serves messages to consumers.  
- **Producer**: Sends messages to Kafka topics.  
- **Consumer**: Reads messages from Kafka topics.  
- **Zookeeper** (for Kafka 2.x): Manages cluster metadata and leader election.  
- **Topics & Partitions**: Messages are distributed across partitions for scalability and parallel processing.  

### 16. What are the key differences between SonicMQ and Kafka?

| Feature       | SonicMQ                  | Kafka                          |
|---------------|--------------------------|--------------------------------|
| **Messaging** | JMS-based                | Distributed log-based          |
| **Persistence** | Supports persistent/non-persistent | Persistent by default          |
| **Scalability** | Limited                 | Highly scalable                |
| **Use Case**  | Enterprise legacy apps   | High-throughput streaming systems |


### 17. Can you share some examples of complex AWS cloud infrastructure issues you faced and how you resolved them?

- **Issue:** Auto Scaling Group not launching instances  
  - **Resolution:** Checked IAM roles and Launch Template configuration.  

- **Issue:** ELB not routing traffic  
  - **Resolution:** Fixed security group and subnet configuration issues.  

- **Issue:** Lambda failing due to missing environment variables  
  - **Resolution:** Added proper secret references and environment variables.  

- **Issue:** RDS connection limits  
  - **Resolution:** Increased `max_connections` and tuned application connection pooling.
 

### 18. Why do you deploy applications both on Docker (standalone) and Kubernetes? What’s the reasoning?

- **Docker Standalone:**  
  - Simple testing and development  
  - Local debugging without cluster dependency  

- **Kubernetes:**  
  - Production-grade deployments  
  - High availability and scalability  
  - Rolling updates and automated recovery  

- **Flexibility:**  
  - Developers can test locally using Docker without needing the full cluster  

---

### 19. Where do you store and manage application secrets in your environment?

### Options used:
- **AWS Secrets Manager**  
- **HashiCorp Vault**  
- **Kubernetes Secrets** (with encryption at rest)  

### Best Practices:
- Avoid hardcoding secrets in code or Dockerfiles  
- Use **environment variables** or **mounted secrets** in pods  
- **Rotate secrets regularly**  

