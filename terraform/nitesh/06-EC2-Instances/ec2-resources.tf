#Plan

# variable "ec2_key_pair" {
#   default = "/Users/nitesh-mac/Desktop/nitesh-devops/terraform/nitesh/06-EC2-Instances/key.pem"
#   #default = "/Users/nitesh-mac/aws/aws_keys/aws_keypair.pem"
# }

resource "aws_key_pair" "deployer" {
  key_name   = "nitesh-key"
  #public_key = "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCcSrYaVHWXxXB6Gd1ESYfHwl3ukpakq7Dnjf5BSqHyQJcJnzy1FFvA4oyhjwELbdhgGXIUyxabWIMFexH1YVv0o3C4P1piNsGTRJQyg2btWMcFAhZ+2P/aElZ394WBANqYMkpLMKtIesddiAJ1MHvHycsRSSmhr7xrNAuFHMmRDImxW4rjyycRFxpUK27xzxyFPELh1EY+7RBS6z4TEnVI6Wh+u7FGm12rtP1qvBqJJmFyb5VGVCNV1UKKnrue8cDkfgV8FVBIlflo6mdvOq0cLeCzkveTIr/IyMZVMoQiLVhc3av4rZe79udaj3+7gPt0ijk5yGH6roOeJQmN9Dz/ nitesh-mac@niteshs-iMac.local"
  public_key = file("~/.ssh/id_rsa.pub")
}

resource "aws_instance" "terraform-ec2-instance" {

  ami                    = data.aws_ami.aws_linux_latest.id
  key_name               = "nitesh-key"
  instance_type          = var.instance_type
  vpc_security_group_ids = [aws_security_group.from-terraform-security-group.id]
  subnet_id              = tolist(data.aws_subnet_ids.subnet_ids.ids)[0]

  connection {
    type = "ssh"
    host = self.public_ip
    user = "ec2-user"
    private_key = file("~/.ssh/id_rsa")
    #private_key = ${file(var.ec2_key_pair)}
  }
  provisioner "remote-exec" {
    inline = [
      "sudo yum install httpd -y",
      "sudo service httpd start",
      "echo Welcome nitesh-devops,Virtual server is at ${self.public_dns} | sudo tee /var/www/html/index.html"
    ]
    
  }

}
