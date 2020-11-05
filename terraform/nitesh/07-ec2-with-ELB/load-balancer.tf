resource "aws_elb" "classic-load-balancer" {
  name            = "tf-classic-load-balancer"
  subnets         = data.aws_subnet_ids.subnet_ids.ids
  security_groups = [aws_security_group.elb_security_group.id]
  instances       = values(aws_instance.terraform-ec2-instance).*.id

  listener {
    instance_port     = 80
    instance_protocol = "http"
    lb_port           = 80
    lb_protocol       = "http"
  }

}


output "elb_public_dns" {
  value = aws_elb.classic-load-balancer
}