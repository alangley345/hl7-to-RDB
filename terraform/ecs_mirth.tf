resource "aws_ecs_cluster" "mirth" {
  name = "hl7-to-rbd mirth"

  setting {
    name  = "containerInsights"
    value = "enabled"
  }
}