variable "cluster_name" {
  description = "Name of the EKS cluster"
  type        = string
}

variable "cluster_version" {
  description = "EKS Kubernetes version"
  type        = string
  default     = "1.27"
}

variable "subnets" {
  description = "Subnets for EKS cluster"
  type        = list(string)
}

variable "vpc_id" {
  description = "VPC ID for EKS cluster"
  type        = string
}

variable "node_instance_type" {
  description = "Instance type for worker nodes"
  type        = string
  default     = "t3.medium"
}
