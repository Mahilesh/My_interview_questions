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


4. Static IP vs Dynamic IP
- Static IP: Manually assigned, doesn’t change over time (e.g., useful for DNS, VPN).
- Dynamic IP: Automatically assigned by DHCP and may change periodically.
- ✅ Use static IPs when consistency is important. Useful for whitelisting and DNS mapping

5. Private Ip is not visible, we should use only public ip but needs to be restricted How?
- Associate Elastic IP (public) with instance
- Use Security Groups/NACLs to allow traffic only from whitelisted IPs or CIDRs.
- Use NACLs or AWS WAF for additional filtering
- Optionally, use VPN or Bastion Host for additional control.

6. Why your org consider Autoscaling instead of Reserved Spot instances
- Auto Scaling provides:
    Elasticity: Adds/removes instances based on load.
    Availability: Maintains healthy instance count.
- Reserved instances save cost but don’t scale.
- Spot instances are cheap but can be interrupted anytime.
✅ So Auto Scaling = balance between cost, scalability, and availability.

7. Terraform Architecture
Core components:
    - Terraform CLI
    - Provider plugins (AWS, Azure, etc.)
    - .tf files = Configuration
    - State file = Infrastructure snapshot
- Workflow: Write → Plan → Apply → Maintain

8. Diff bt main.tf vs terraform.statefile vs terraform.tfvar file 
File	                        Purpose
main.tf	                    Main configuration file (resource definitions)
terraform.tfvars	        Variable values (like region, instance type)
terraform.tfstate	        Stores infrastructure state (actual resource info)

10. Gitlab CICD - Write yaml file for rollout/rollback deployment in gitlab CICD?

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

11. what is Terraform statefile
- .tfstate file stores current state of your infra.
- Helps Terraform track resource changes and perform diffs.
- Don’t edit manually. Store in remote backend like S3 with locking via DynamoDB.
  
12. diff bt TCP vs UDP?
TCP	                        UDP
==================      ============== 
Connection-based	    Connectionless
Reliable	            Unreliable
Slower (handshake)	    Faster
Used for HTTP, SSH	    Used for DNS, streaming

14. What is TLS?
- TLS (Transport Layer Security) = Encrypts data during transmission.
- Replaces SSL.
- Ensures confidentiality, integrity, authenticity of data between client-server.

15. How you reduced monthly costs by 20% through EC2? (from resume)
16. How do you create kubernetes cluster through terraform - whether you used CICD for that
17. DNS is not working in Linux - How to check connectivity and trobuleshoot the issue
18. Developer somehow saw the secret which is hardcoded, Are you able to modify and make it invisble WITHOUT RESTART? if yes, How?
19. Port no 8080 mapped to one instance and 443 mapped to other instances - how do you find which is public and private?
20. Error code - 404 - what it means?
21. Write a shell script - which you written recently?
22. Diff bt git merge vs git rebase
