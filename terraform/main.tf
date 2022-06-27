provider "aws" {
  region  = "us-east-1"
}

#define location of state file
terraform {
  backend "s3" {
    bucket = "myterraformcode"
    key    = "prod/hl7-to-rdb.tfstate"
    region = "us-east-1"
  }

}