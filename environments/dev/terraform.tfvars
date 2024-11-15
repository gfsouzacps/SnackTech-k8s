project_name       = "k8s-dev"
cidr_block         = "10.0.0.0/16"
subnet_cidrs       = ["10.0.1.0/24", "10.0.2.0/24"]
availability_zones = ["us-east-1"]
cluster_name       = "dev-cluster"
cluster_version    = "1.27"
node_instance_type = "t3.medium"
