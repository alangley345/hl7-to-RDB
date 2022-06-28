resource "aws_ecs_cluster" "foo" {
  name = "hl7-to-rbd mirth"

  setting {
    name  = "containerInsights"
    value = "enabled"
  }
}