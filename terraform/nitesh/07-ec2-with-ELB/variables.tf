
variable "instance_type" {
  default = "t2.micro"
}

variable "instance_owners" {
  default = "amazon"
}
variable "private_key_rsa" {
  default = "~/.ssh/id_rsa"
}