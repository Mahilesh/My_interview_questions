Company wise - I will upload the questions & answers

## 📚 Table of Contents

- [MIRAFRA - Bangalore (L1 - virtual)](#mirafra---bangalore-l1---virtual)
- [Eurofins India IT Solutions - Bangalore (L1 - virtual)](#eurofins-india-it-solutions---bangalore-l1---virtual)
- Siemens - Face to Face
- Capgemini (L1 - virtual)]
- Sigma L1 - virtual
- SqaureShift - Face to Face


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

# Sigma - L1 -virtual - Questions

1. What is the difference between Docker and Kubernetes?
2. How do you run multiple containers in Docker?
3. How do you upgrade the Kubernetes cluster version?
4. Which Kubernetes services have you worked with?
5. What is the difference between a Deployment and a StatefulSet in Kubernetes?
6. What is the default service type in Kubernetes?
7. If Docker doesn’t provide container orchestration, which tool is used for that?
8. Have you worked with Kubernetes Operators?
9. What tasks do you perform in SonarQube within a Jenkins pipeline?
10. Do you know how to write a Jenkinsfile?
11. Can you explain the CI/CD workflow you follow?
12. Which Linux commands or features have you worked with most?
13. Apart from Tomcat, which web servers do you know and have experience with?
14. If an application shows as DOWN in the browser, how would you troubleshoot it from the server?
15. Inside /var/log, which files would you check to debug server issues?
16. Does your company have separate teams for Terraform, Kubernetes, and Docker?
17. Do you have knowledge of databases?
18. A junior DevOps engineer deployed a container, but after 5 days the container is down and the data is lost. How would you modify the Dockerfile to prevent data loss in the future?


# Sigma - L1 -virtual - Questions with answers

**1. Difference between Docker and Kubernetes:**

* Docker: Container platform to build, ship, and run applications.
* Kubernetes: Container orchestration platform to manage multiple containers, scale apps, handle load balancing, and self-healing.

**2. How to run multiple containers in Docker:**

* Use `docker run` for multiple containers manually:

```
docker run -d --name app1 myapp:1.0
docker run -d --name app2 myapp:1.0
```

* Or use Docker Compose for multiple services.

**3. How to upgrade Kubernetes cluster version:**

* EKS: `eksctl upgrade cluster --name <cluster-name> --version <new-version>`
* Kubeadm:

```
kubeadm upgrade plan
kubeadm upgrade apply <version>
```

* Upgrade master first, then worker nodes, then update kubelet & kubectl.

**4. Kubernetes services you’ve worked with:**

* ClusterIP – internal communication
* NodePort – expose service on node port
* LoadBalancer – external access via cloud LB

**5. Difference between Deployment and StatefulSet:**

| Feature  | Deployment           | StatefulSet                           |
| -------- | -------------------- | ------------------------------------- |
| Pods     | Identical, stateless | Stable network ID & storage, stateful |
| Scaling  | Simple               | Maintains order & identity            |
| Use case | Web servers          | Databases, messaging queues           |

**6. Default service type in Kubernetes:**

* ClusterIP (accessible only within the cluster).

**7. Docker doesn’t provide container orchestration. Tool used:**

* Kubernetes, Docker Swarm, or OpenShift.

**8. Have you worked with Kubernetes Operators:**

* Yes/No. Operators automate management of custom apps, handling deployments, upgrades, and recovery.

**9. Tasks performed in SonarQube within Jenkins pipeline:**

* Code quality analysis
* Run static code scans
* Break build if quality gates fail

**10. Writing a Jenkinsfile:**

* Yes. Can write Declarative or Scripted pipelines with stages like build, test, deploy, and integrate tools like SonarQube, Docker, Kubernetes.

**11. CI/CD workflow:**

1. Code commit: Push code to GitHub/GitLab.
2. Build stage: Jenkins pulls code, runs build and unit tests.
3. Code quality scan: SonarQube evaluates code.
4. Docker build: Package application into a container image.
5. Deploy stage: Deploy to Kubernetes or test server.
6. Monitoring & alerting: Ensure application health post-deployment.

**12. Linux commands/features you’ve worked with:**

* File commands: `ls, cp, mv, rm, find`
* Process & service: `ps, top, systemctl, service`
* Disk & memory: `df, du, free, vmstat`
* Network: `ping, netstat, ss, telnet, nc`
* Logs: `tail, less, journalctl`
* Shell scripting & cron jobs

**13. Apart from Tomcat, web servers known:**

* Apache HTTP Server, Nginx, JBoss, WildFly

**14. Troubleshooting DOWN applications from server:**

1. Check service status: `systemctl status <service>`
2. Check logs: `/var/log/<service>/` or app logs
3. Check port availability: `netstat -tulnp | grep <port>`
4. Check resource usage: `top`, `df -h`, `free -m`
5. Check dependencies: DB connections, environment variables, configuration files

**15. /var/log files to check for server issues:**

* `/var/log/messages` or `/var/log/syslog` – general system errors
* `/var/log/secure` or `/var/log/auth.log` – authentication
* `/var/log/httpd/` or `/var/log/nginx/` – web server errors
* `/var/log/mysqld.log` – database errors
* `/var/log/cron` – cron jobs

**16. Separate teams for Terraform, Kubernetes, Docker:**

* Small teams manage all; larger orgs may have specialized teams.

**17. Knowledge of databases:**

* MySQL, PostgreSQL, Oracle; basic queries, backup, restore, connection checks.

**18. Preventing data loss in Docker container:**

* Use volumes to persist data outside the container:

```dockerfile
VOLUME /var/lib/mysql
```

* Or mount host directories:

```bash
docker run -v /host/data:/container/data myapp:1.0
```

* Ensures data is preserved even if the container is deleted.

### SqaureShift - Face to Face

# Elasticsearch & Kubernetes Interview Questions and Answers

## Elasticsearch & Deployment Related

**1. Are you running Elasticsearch on-premises or using Elastic Cloud on Kubernetes (ECK)?**  
We’re using Elasticsearch deployed on-premises within Kubernetes, not Elastic Cloud. We manage it using Helm charts or the Elastic Cloud on Kubernetes (ECK) operator depending on the environment. ECK simplifies the management of Elasticsearch clusters including scaling, upgrades, and monitoring through CRDs.

**2. Which version of open-source Elasticsearch are you currently using?**  
We’re using the open-source Elasticsearch 8.x version (for example, 8.10). This version includes improved security by default (TLS, built-in authentication) and enhanced performance for large-scale indexing and search workloads.

**3. How do you deploy the ELK stack (Elasticsearch, Logstash, Kibana) in Kubernetes — for example, how do you handle components like Filebeat (as a DaemonSet)?**  
We deploy the ELK stack using Helm charts or manifests:
- Elasticsearch – as a StatefulSet (since it’s stateful and requires persistent storage).
- Logstash – as a Deployment (stateless, can scale horizontally).
- Kibana – as a Deployment with an internal Service.
- Filebeat – deployed as a DaemonSet on each node to collect logs and forward them to Logstash/Elasticsearch.  
Configuration and secrets (like credentials) are managed through ConfigMaps and Secrets in Kubernetes.

**4. Have you encountered any recent issues or performance challenges with Elasticsearch in your project? How did you resolve them?**  
Yes, we faced indexing slowness and high heap memory usage on data nodes. We resolved it by:
- Increasing JVM heap size in the StatefulSet YAML.
- Optimizing index settings (reduced number of shards, used ILM policies).
- Offloading heavy queries to non-peak hours.
- Implementing Prometheus + Grafana monitoring for Elasticsearch metrics to identify bottlenecks early.

**5. Is your Elasticsearch cluster exposed externally (public access) or restricted for internal access only?**  
It’s restricted for internal access only. We expose Kibana via Ingress (HTTPS) for internal users and restrict Elasticsearch access through NetworkPolicies and RBAC. No direct public access is allowed for security reasons.

## Kubernetes Concepts & Architecture

**6. What types of services are commonly used in your Kubernetes setup (e.g., ClusterIP, NodePort, LoadBalancer, etc.)?**  
We mainly use:
- ClusterIP – for internal communication between microservices.
- NodePort – for limited external access in non-production.
- LoadBalancer – for production services through an external load balancer (e.g., AWS ALB).
- Headless Service – for StatefulSets like Elasticsearch to enable direct Pod-to-Pod communication.

**7. Can you explain how networking works in Kubernetes — for example, how Pods, Services, and Ingress communicate?**  
Each Pod gets its own IP. Services (like ClusterIP) provide a stable endpoint to access Pods behind them. Ingress acts as a Layer 7 HTTP reverse proxy that routes external traffic to internal Services based on rules. All Pods can communicate with each other within the same cluster via the CNI (Container Network Interface).

**8. How do different Kubernetes components communicate with each other (e.g., kube-apiserver, kubelet, controller manager)?**  
The kube-apiserver is the central control plane — all communication passes through it. The kubelet on each node communicates with the API server to report Pod status and receive instructions. The controller manager and scheduler continuously interact with the API server to ensure the desired cluster state is maintained. Communication happens securely via HTTPS and certificates.

**9. What’s the difference between a Pod and a Container in Kubernetes?**  
A Container is a single runnable unit (like a process) created from an image. A Pod is the smallest deployable unit in Kubernetes that can hold one or more containers sharing the same network namespace and storage volumes. Pods enable containers to communicate easily via localhost.

**10. What’s the difference between a StatefulSet and a Deployment (Stateless application)?**  
A Deployment manages stateless applications — Pods are identical and can be replaced anytime. A StatefulSet manages stateful applications — each Pod has a unique identity and persistent storage. Elasticsearch, Kafka, and databases typically use StatefulSets.

## Configuration, Security & Validation

**11. How do you integrate Kubernetes with Vault or a Secret Manager? Where do you specify secret references in your manifests?**  
We integrate HashiCorp Vault (or AWS Secrets Manager) with Kubernetes using sidecar injectors or CSI driver. Secrets are fetched dynamically and mounted as environment variables or volumes. In manifests, we specify secret references under:
```yaml
envFrom:
  - secretRef:
      name: my-app-secrets
```
or using a Vault Agent injector annotation on the Pod definition.

12. How do you implement Role-Based Access Control (RBAC) in your Kubernetes cluster?
We define Roles/ClusterRoles to specify permissions (e.g., get, list, create on Pods). RoleBindings/ClusterRoleBindings link those roles to specific users, groups, or service accounts. This ensures least privilege and prevents unauthorized API access.

13. What are the key sections typically defined inside a deployment.yaml file?
A standard deployment.yaml includes:

apiVersion, kind, metadata

spec:

replicas

selector

template:

metadata (labels)

spec:

containers: name, image, ports, env, resources, volumeMounts

volumes

imagePullSecrets, tolerations, affinity, etc.

14. After deploying an application in Kubernetes, how do you verify that it’s running correctly and healthy?
After deployment, I typically:

Check rollout status → kubectl rollout status deployment/<name>

Verify Pod health → kubectl get pods -o wide

Inspect logs → kubectl logs <pod-name>

Describe resources for troubleshooting → kubectl describe pod <pod-name>

Validate service and ingress endpoints using curl or browser.
For ongoing checks, readiness/liveness probes are defined in the YAML.

15. Do you use Kustomize for environment-specific configurations in your CI/CD pipeline (e.g., GitLab)?
Yes, we use Kustomize with GitLab CI/CD to manage environment overlays — like dev, test, and prod. Each environment has its own overlay with specific ConfigMaps, Secrets, and replica counts. This helps maintain one base manifest and customize per environment efficiently.
