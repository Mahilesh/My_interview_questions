# My_interview_questions
Company wise - I will upload the questions

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

### Eurofins India IT Solutions - Bangalore (L1 - virtual)

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

