resource "aws_ecs_cluster" "mirth" {
  name = "hl7_to_rdb_mirth"

  setting {
    name  = "containerInsights"
    value = "enabled"
  }
}

resource "aws_ecs_service" "mirth" {
  name            = "mirth_engine"
  cluster         = aws_ecs_cluster.mirth.id
  task_definition = aws_ecs_task_definition.mirth.arn
  desired_count   = 1
  iam_role        = aws_iam_role.foo.arn
  depends_on      = [aws_iam_role_policy.foo]

  ordered_placement_strategy {
    type  = "binpack"
    field = "cpu"
  }

  load_balancer {
    target_group_arn = aws_lb_target_group.foo.arn
    container_name   = "mongo"
    container_port   = 8080
  }

  placement_constraints {
    type       = "memberOf"
    expression = "attribute:ecs.availability-zone in [us-west-2a, us-west-2b]"
  }
}