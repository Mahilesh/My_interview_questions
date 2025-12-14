Summary 
=======
1. Mirafra - (L1 - virtual)
2. Eurofins - (L1 - virtual)
3. Siemens - (L1 - Face to Face)
4. Capgemini - (L1 - virtual)
5. Sigma - (L1 - virtual)
6. SquareShift - (L1 - Face to Face)
7. Expleo - (L1 - Virtual) - Fully ON-Premises - Not relevant
8. Tech Mahindra - (L1 - virtual)
9. BMW TechWorks - (L1 - virtual) - Operations Support Role - Not relevent
10. Neeve AI - Screening Interview (L1 - Virtual)
11. Akamai - (L1 - Virtual)
12. Sopra Steria - (L1 - Virtual)

Mirafra
=======
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


Eurofins
========
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

Siemens
========
1. Can you introduce yourself?
2. What are your day-to-day activities as a DevOps engineer?
3. You mentioned AWS cost optimization in your resume — how did you achieve that?
4. What is a target policy in IAM?
5. If Commit A was done by someone else and Commit B was done by you, which Git command would you use to commit your changes (Commit B)?
6. What AWS services have you worked with?
7. Can you explain a recent issue you faced in GitLab CI/CD?
8. What are the remote backends available for storing a Terraform state file?
9. How do you implement a remote backend in Terraform?
10. Have you completed any AWS certifications?
11. In Kubernetes, are worker nodes managed by you or by Kubernetes itself?
12. How do you perform cost optimization in AWS in practice?
13. Which version of Terraform are you currently using?

Capgemini
==========
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


Sigma
======
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

SquareShift
===========
1.	Are you running Elasticsearch on-premises or using Elastic Cloud on Kubernetes (ECK)?
2.	Which version of open-source Elasticsearch are you currently using?
3.	How do you deploy the ELK stack (Elasticsearch, Logstash, Kibana) in Kubernetes — for example, how do you handle components like Filebeat (as a DaemonSet)?
4.	Have you encountered any recent issues or performance challenges with Elasticsearch in your project? How did you resolve them?
5.	Is your Elasticsearch cluster exposed externally (public access) or restricted for internal access only?
6.	What types of services are commonly used in your Kubernetes setup (e.g., ClusterIP, NodePort, LoadBalancer, etc.)?
7.	Can you explain how networking works in Kubernetes — for example, how Pods, Services, and Ingress communicate?
8.	How do different Kubernetes components communicate with each other (e.g., kube-apiserver, kubelet, controller manager)?
9.	What’s the difference between a Pod and a Container in Kubernetes?
10.	What’s the difference between a StatefulSet and a Deployment (Stateless application)?
11.	How do you integrate Kubernetes with Vault or a Secret Manager? Where do you specify secret references in your manifests?
12.	How do you implement Role-Based Access Control (RBAC) in your Kubernetes cluster?
13.	What are the key sections typically defined inside a deployment.yaml file?
14.	After deploying an application in Kubernetes, how do you verify that it’s running correctly and healthy?
15.	Do you use Kustomize for environment-specific configurations in your CI/CD pipeline (e.g., GitLab)?3


Tech Mahindra
==============
1. Tell me about yourself 
2. How would you establish communication between two VPCs? Describe common methods and when to use each.
3. Have you written end-to-end Kubernetes manifests? If yes, describe an example (what manifests you created and why).
4. Describe a recent issue or challenge you faced with the ELK stack and how you diagnosed and resolved it.
5. Describe a recent issue or challenge you faced with Kafka and how you diagnosed and resolved it.
6. What is Docker networking? Explain the different network drivers and when to use them.
7. What typically goes inside a Dockerfile? List the common instructions and their purposes.
8. How do you containerize an application using a Dockerfile? Walk me through the steps from source to image.
9. How do you persist data for Docker containers? Explain volumes, bind mounts, and other options.
10. What are AWS security best practices? Cover identity, access, network, and data protection.
11. What is the difference between stateless and stateful applications? Give examples and implications for scaling.
12. What is the purpose of the Terraform state file and why is it important?
13. What is Ansible, what is it used for, and what are its key components (playbooks, inventory, modules)?
14. What are Kubernetes manifests and which types of manifests are commonly used (e.g., Deployment, Service, ConfigMap)?
15. What is a CrashLoopBackOff (CrashBackLoop) and how would you troubleshoot it?
16. In which Kubernetes manifest do you specify the number of replicas? (Explain where and how.)
17. What is the difference between IAM roles and IAM policies in AWS? Give an example of each.
18. How would you create an EKS cluster? Explain the step-by-step process and tools you’d use.
19. Have you set up alerts in the ELK stack? If yes, explain how you implemented alerting and what you monitored.

Neeve AI
=========
1. Tell me about yourself and describe the key projects you are currently working on.
2. Can you explain what Blue-Green Deployment is and how it works?
3. Do you work in rotational shifts or a general day shift?
4. What responsibilities do you handle in Kubernetes, and which Kubernetes objects do you work with regularly?
5. Are you using Helm charts for deployments? If yes, how?
6. Do you use ArgoCD, or do you rely on another CI/CD tool for deployments?
7. Are you comfortable working on Python-based projects or writing Python automation scripts?
8. What monitoring stack or tools are currently used in your organization?
9. Can you explain your involvement and responsibilities in managing or maintaining Jenkins?


Akamai
======
1. Can you tell me about yourself?
2. What experience do you have with Linux, including troubleshooting and scripting?
3. Which Linux distribution do you mostly work with?
4. What is the difference between Docker and Podman?
5. Are you familiar with Podman?
6. What is the difference between a bind mount and a volume mount?
7. Have you heard of user namespaces in Linux?
8. What are the fundamentals of Docker?
9. If my OS is Windows, can I run Linux containers on it? How?
10. Have you heard of the /etc/passwd file in Linux?
11. In a Bash script, how would you delete log folders older than 30 days?
12. What is a Terraform workspace?
13. What is the restart policy in Docker?
14. What does HTTP status code 404 mean?
15. What does HTTP status code 403 mean?
16. What does HTTP status code 200 mean?
17. What is a Virtual Host in Apache?
18. Is GitLab deployed as a container or on a virtual machine in your environment?
19. How do you secure the GitLab HTTPS URL in AWS?
20. How do you manage RBAC in GitLab for application teams?
21. How do you manage LDAP integration?
22. What are taints and tolerations in Kubernetes?
23. How do you maintain state in Terraform?
24. If infrastructure is created using Terraform and someone manually modifies a security group in AWS, how do you handle it and apply future changes?
25. How do you troubleshoot network issues in AWS? What steps do you take at the VPC and service level?
26. How do you configure a reverse proxy for a Tomcat application?
27. How would you design and enable communication between frontend, backend, and database in a three-tier architecture on on-premises VMs?
28. How would you design and enable communication between frontend, backend, and database in a three-tier architecture using Docker?
29. How would you design and enable communication between frontend, backend, and database in a three-tier architecture using Kubernetes?
30. Do you use ClusterIP services in Kubernetes?
31. How do you expose your application to the internet?
32. What is the difference between RabbitMQ and SonicMQ?
33. What is a CrashLoopBackOff error in Kubernetes?
34. Have you created a Kubernetes cluster from scratch, or are you managing an existing one?
35. In Terraform, there is also a concept called taint. Are you familiar with it?
36. What is a ClusterRoleBinding in Kubernetes?
37. What monitoring tools have you worked with?
38. Have you used Splunk?
39. Can you explain Prometheus and how you configured it in your project?
40. What is Node Exporter?
41. In Prometheus, what additional steps are required to deeply monitor a backend application, such as a Java-based app?
42. A Docker container keeps restarting continuously. How would you troubleshoot this issue?
43. How do applications running in different Docker networks communicate with each other?
44. How do you optimize your Docker images?
45. What is the standard and secure way to store secrets?
46. In Kubernetes, how do you manage secrets and what are the best practices?
47. In Docker, how do you manage secrets and what are the best practices?
48. How do you integrate Kubernetes with AWS Secrets Manager to read secrets in Kubernetes YAML files?
49. Have you created a complete VPC end-to-end?
50. If the frontend cannot communicate with the backend (and vice versa), what commands would you use to troubleshoot?
51. What is a Persistent Volume in Kubernetes?
52. Have you heard of cgroups?
53. What is the difference between the COPY and ADD commands in Docker?
54. Which is the best practice to use in a Dockerfile: COPY or ADD, and why?
55. If you need to download files from a remote URL, can you use the COPY command?
56. What does docker prune mean?
57. Have you heard of overlay networking in Docker?
58. What is the difference between Docker image layers and overlay?  and /var/lib/docker/overlay vs /var/lib/docker/layers
59. Have you created a multi-stage Dockerfile? If yes, how?

Sopra Steria
=============
1. Can you explain your role in your current company, the infrastructure you work on, and the projects you handle?
2. Have you faced any high-priority (P1/P2) incidents so far? How did you troubleshoot and resolve them?
3. What is the difference between a Kubernetes master (control plane) node and a worker node? What components run on each?
4. How does the Kubernetes scheduler decide on which node a pod should be placed?
5. What are stateful and stateless applications in Kubernetes? Can you give examples?
6. What is the kubectl drain command, and what happens when you execute it on a node?
7. What is kubectl cordon, and how is it different from kubectl drain?
8. What is node affinity in Kubernetes, and why is it used?
9. How do you check the health of etcd in a Kubernetes cluster?
10. What is the difference between a ConfigMap and a Secret in Kubernetes?
11. Have you used any DevOps automation tools? If yes, which tools and for what purpose?
12. Have you deployed GitLab as a self-hosted setup? If yes, can you explain the architecture?
13. What is terraform taint, and when would you use it?
14. If an EC2 instance was created manually earlier, and now you are asked to increase its RAM using Terraform, how would you handle this situation?
15. How do you protect Terraform-managed resources from accidental deletion?
16. Have you used Ansible? What kind of tasks have you automated using it?
17. How do you manage and secure secrets in Ansible?
18. In an Ansible playbook, how do you make the play wait until a server reboot is fully completed before running the next task?
19. What are some basic Linux commands you use to check memory, CPU, disk usage, and system performance?
