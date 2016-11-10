
variable "aws_key_name"  {
  default = "home"
}

variable "aws_region" {
  description = "AWS region to launch servers."
  default     = "us-west-1"
}

# Ubuntu Precise 12.04 LTS (x64)
variable "aws_amis" {
  default = {
    eu-west-1 = "ami-9398d3e0"
    us-east-1 = "ami-b73b63a0"
    us-west-1 = "ami-23e8a343"
    us-west-2 = "ami-5ec1673e"
  }
}
