output "MY_USER_IAM_NAME" {
    value = aws_iam_user.my_user_iam["abc"].name
        
}

# output "MY_USER_IAM_ARN" {
#     value = aws_iam_user.my_user_iam.arn
# }


# output "MY_USER_IAM_UID" {
#     value = aws_iam_user.my_user_iam.unique_id
# }

# output "MY_USER_IAM_PATH" {
#     value = aws_iam_user.my_user_iam.path
# }