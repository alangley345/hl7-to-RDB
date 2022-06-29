resource "aws_iam_role" "mirth-instance" {
  name = "Mirth_Service"

  assume_role_policy = <<EOF
{
  "Version": "2008-10-17",
  "Statement": [
    {
      "Sid": "",
      "Effect": "Allow",
      "Principal": {
        "Service": "ec2.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
EOF
}

#resource "aws_iam_role_policy" "mirth_instance_policy" {
#  name = "Mirth_Instance_Policy"
#  role = aws_iam_role.mirth-instance.id 
#  description = "ec2 access for mirth-instance"
#  policy = jsonencode(
#    {
#    "Version":"2012-10-17"
#    "Statement": [
#        {
#            "Sid": "",
#            "Effect": "Allow",
#            "Principal": {
#            "Service": "ec2.amazonaws.com"
#                    },
#                    "Action": "sts:AssumeRole"
#                }
#            ]
#        }
#    ]
#  })
#}