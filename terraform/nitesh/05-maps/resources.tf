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
#Defining lists to set variables
#Supports any,string,number,tuple,set,map,bool
variable "users" {
  default = {
    "abc" : { country : "Malaysia", department : "abc" },
    "pqr" : { country : "Australia", department : "pqr" },
    "xyz" : { country : "INDIA", department : "xyz" }
  }
}

#Plan

resource "aws_iam_user" "my_user_iam" {

  for_each = var.users

  name = each.key
  tags = {
    country    = each.value.country
    department = each.value.department
  }
}
