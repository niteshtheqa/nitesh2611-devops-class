
output "AWS_S3_BUCKET_VERSIONING" {
  value = aws_s3_bucket.my_s3_bucket.versioning[0].enabled
}

output "AWS_S3_BUCKET_ARN" {
  value = aws_s3_bucket.my_s3_bucket.arn
}
