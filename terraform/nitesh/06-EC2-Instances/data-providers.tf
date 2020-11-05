data "aws_subnet_ids" "subnet_ids" {
  vpc_id = aws_default_vpc.default.id
}

data "aws_ami" "aws_linux_latest" {
  most_recent = true
  owners      = [var.instance_owners]
  filter {
    name   = "name"
    values = ["amzn2-ami-hvm-*"]
  }
}