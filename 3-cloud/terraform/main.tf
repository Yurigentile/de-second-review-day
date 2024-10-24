
terraform {
  required_providers {
    #TODO: aws will be a required provider here
      aws = {
        source  = "hashicorp/aws"
        version = "~> 4.16"
    }
  }

  required_version = ">= 1.2.0"
}

 
#TODO: add a 'provider' block for aws here 

provider "aws" {
  access_key =
  secret_key =
  region  = "eu-west-2"
}


data "aws_caller_identity" "current" {}


data "aws_region" "current" {
  name = "eu-west-2"
}
