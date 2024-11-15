import unittest
from terraform import Terraform

class TestEKS(unittest.TestCase):
    def setUp(self):
        self.tf = Terraform(working_dir="../environments/dev")
        self.tf.init()

    def test_eks_cluster(self):
        plan = self.tf.plan(out="plan.out")
        self.assertIn("aws_eks_cluster", plan, "EKS Cluster resource not found in plan")

    def tearDown(self):
        self.tf.destroy(auto_approve=True)

if __name__ == "__main__":
    unittest.main()
