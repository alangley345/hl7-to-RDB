resource "aws_ecs_cluster" "mirth" {
  name = "hl7_to_rdb mirth"

  setting {
    name  = "containerInsights"
    value = "enabled"
  }
}