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
  requires_compatibilities = ["FARGATE"]
  #task_role_arn            = "${var.ecs_task_role}"
  #execution_role_arn       = "${var.ecs_task_execution_role}"
  network_mode             = "awsvpc"
  cpu                      = "100"
  memory                   = "256"

  container_definitions = <<DEFINITION
    [
      {
        "image": "https://dockerhub.io/r/nextgenhealth/connect:latest",
        "name": "mirth-connect",
        "logConfiguration": {
                    "logDriver": "awslogs",
                    "options": {
                        "awslogs-region" : "us-east-1",
                        "awslogs-group" : "fargate-logs",
                        "awslogs-stream-prefix" : "mirth"
                    }
                }
      }
    ]
  DEFINITION
}

#resource "aws_ecs_task_set" "mirth" {
# service         = aws_ecs_service.mirth.id
# cluster         = aws_ecs_cluster.mirth.id
# task_definition = aws_ecs_task_definition.mirth.arn
# launch_type     = FARGATE
#}
