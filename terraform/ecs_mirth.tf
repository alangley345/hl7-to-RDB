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

  ordered_placement_strategy {
    type  = "binpack"
    field = "cpu"
  }

  placement_constraints {
    type       = "memberOf"
    expression = "attribute:ecs.availability-zone in [us-west-2a, us-west-2b]"
  }
}

resource "aws_ecs_task_definition" "mirth" {
  family = "hl7_to_rdb_mirth"
  requires_compatibilities = ["EC2"]
  container_definitions = jsonencode([
    {
      name      = "mirth"
      image     = "https://hub.docker.com/r/nextgenhealthcare/connect:latest"
      cpu       = 10
      memory    = 256
      essential = true
      portMappings = [
        {
          containerPort = 8443
          hostPort      = 8443
        }
      ]
    },
  ])

  #volume {
  # name      = "service-storage"
  # host_path = "/ecs/service-storage"
  #}

  placement_constraints {
    type       = "memberOf"
    expression = "attribute:ecs.availability-zone in [us-east-1a, us-east-1b]"
  }
}

#resource "aws_ecs_task_set" "mirth" {
# service         = aws_ecs_service.mirth.arn
# cluster         = aws_ecs_cluster.mirth.arn
# task_definition = aws_ecs_task_definition.mirth.arn
#}