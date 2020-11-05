output "AWS_KEY_ID" {
  value = aws_key_pair.deployer.id
}

output "AWS_KEY_NAME" {
  value = aws_key_pair.deployer.key_name
}

output "AWS_KEY_PUBLIC_KEY" {
  value = aws_key_pair.deployer.public_key
}