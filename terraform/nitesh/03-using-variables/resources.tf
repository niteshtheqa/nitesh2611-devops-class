# Configure the AWS Provider
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 3.0"
    }
  }
}
provider "aws" {
  region = "us-east-2"
}
#Variables
#Supports any,string,number,tuple,set,map,bool
variable "my_s3_bucket" {
  default = "my-s3-bucket-nitesh2611-00"
}
#Plan
resource "aws_s3_bucket" "my_s3_bucket" {
  count  = 2
  bucket = "${var.my_s3_bucket}${count.index}"
  versioning {
    enabled = true
  }
}
