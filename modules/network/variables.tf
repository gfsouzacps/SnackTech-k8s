variable "cidr_block" {
  description = "CIDR block for the VPC"
  type = string
}

variable "subnet_cidrs"{
    description = "CIDR blocks for the subnets"
    type = list(string)
}

variable "availability_zones" {
  description = "List of availability zones"
  type = list(string)
}

variable "project_name" {
  description = "Name of the project"
  type = string
}