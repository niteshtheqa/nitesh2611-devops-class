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
variable "names" {
  default = ["abc","jkl","mno","pqr"]
}
#Plan
# resource "aws_iam_user" "my_user_iam" {
#   count  = length(var.names)
#   name = var.names[count.index]

# }

#Creating resources with For_Each method 
resource "aws_iam_user" "my_user_iam" {

  for_each = toset(var.names)

  name = each.value

}
