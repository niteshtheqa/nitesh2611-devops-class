provider "aws" {
    region = "us-east-2"
    version = "~>2.70"
}

#Plan
resource "aws_s3_bucket" "my_s3_bucket"{
    bucket = "my-s3-bucket-nitesh2611-001"
}

