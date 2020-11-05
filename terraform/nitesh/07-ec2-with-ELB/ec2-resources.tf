#Plan

resource "aws_key_pair" "deployer" {
  key_name   = "nitesh-key"
  public_key = file("~/.ssh/id_rsa.pub")
}

resource "aws_instance" "terraform-ec2-instance" {


  ami                    = data.aws_ami.aws_linux_latest.id
  key_name               = aws_key_pair.deployer.key_name
  instance_type          = var.instance_type
  vpc_security_group_ids = [aws_security_group.from-terraform-security-group.id]
  for_each               = data.aws_subnet_ids.subnet_ids.ids
  subnet_id              = each.value
  tags = {
    name : "http_servers_$(each.value)"
  }


  provisioner "remote-exec" {
    inline = [
      "sudo yum install httpd -y",
      "sudo service httpd start",
      "echo Welcome nitesh-devops,Virtual server is at ${self.public_dns} | sudo tee /var/www/html/index.html"
    ]
    connection {
      type        = "ssh"
      host        = self.public_ip
      user        = "ec2-user"
      private_key = file(var.private_key_rsa)
    }
  }

}
