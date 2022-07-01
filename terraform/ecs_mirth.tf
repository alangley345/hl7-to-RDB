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

  network_configuration {
    subnets          = [aws_subnet.mirth]
    security_groups  = [data.terraform_remote_state.base_state.outputs.production_default_sg]
    assign_public_ip = false
  }

  ordered_placement_strategy {
    type  = "binpack"
    field = "cpu"
  }

}

resource "aws_ecs_task_definition" "mirth" {
  family                   = "hl7_to_rdb_mirth"
  requires_compatibilities = ["FARGATE"]
  #task_role_arn            = "${var.ecs_task_role}"
  #execution_role_arn       = "${var.ecs_task_execution_role}"
  network_mode = "awsvpc"
  cpu          = "256"
  memory       = "512"

  container_definitions = <<DEFINITION
    [
      {
        "image": "https://dockerhub.io/r/nextgenhealth/connect:latest",
        "name": "mirth-connect",
        "cpu": 256
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
