**Clo835 Assignment#1**
**Rohan Pamnani - 178266219**

**Create Dockerfile, build docker image and deploy docker container on Amazon Linux EC2**
Assignment 1: Dockerized Application Deployment on Amazon Linux EC2


### Table of Contents

1. [Deploying EC2 Instance using Terraform](#deploying-ec2-instance-using-terraform)
2. [Building and Pushing Docker Images with GitHub Actions](#building-and-pushing-docker-images-with-github-actions)
3. [Hosting Application and Database Containers on EC2 Instance](#hosting-application-and-database-containers-on-ec2-instance)
4. [Accessing Application Web Pages through Browser](#accessing-application-web-pages-through-browser)

**Deploying EC2 Instance using Terraform**

Initialize Terraform:

clone the repo in your local studio

git init 

git clone https://github.com/178266219-myseneca/clo835-rohanpamnani.git 

go to terraform_code/prod/instances

terraform init

terraform plan

terraform validate

terraform apply


**Using GitHub action**


make all changes in prod branch

protect main branch

git add .

git commit -m " "

git push

docker will trigger workflow and we will merge and pull to trigger in main branch.

**Hosting Application and Database Containers on EC2 Instance**

SSH into the EC2 instance.


Configure AWS credentials using aws configure.


Login to Amazon ECR from the EC2 instance.


Run Docker containers using the docker run command, building them on top of Docker images stored in Amazon ECR.

**Accessing Application Web Pages through Browser)**


Copy the public IP of the EC2 instance.


Open a browser and access the following URLs:


http://<EC2_public_IP>:8081 for the blue app.


http://<EC2_public_IP>:8082 for the pink app.


http://<EC2_public_IP>:8083 for the lime app.





