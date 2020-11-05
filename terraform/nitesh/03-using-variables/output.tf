
output "AWS_S3_BUCKET_VERSIONING" {
  value = aws_s3_bucket.my_s3_bucket[*].versioning[0].enabled
}

output "AWS_S3_BUCKET_ARN" {
  value = aws_s3_bucket.my_s3_bucket[*].arn
}

output "AWS_S3_BUCKET_ACL" {
  value = aws_s3_bucket.my_s3_bucket[*].acl
}


output "AWS_S3_BUCKET_HOSTED_ZONE_ID" {
  value = aws_s3_bucket.my_s3_bucket[*].hosted_zone_id
}


output "AWS_S3_BUCKET_BUCKET_REGIONAL_DOMAIN_NAME" {
  value = aws_s3_bucket.my_s3_bucket[*].bucket_regional_domain_name
}


output "AWS_S3_BUCKET_BUCKET_DOMAIN_NAME" {
  value = aws_s3_bucket.my_s3_bucket[*].bucket_domain_name
}
