import unittest
from terraform import Terraform

class TestNetwork(unittest.TestCase):
    def setUp(self):
        # Carrega o módulo Network
        self.tf = Terraform(working_dir="../modules/network")
        self.tf.init()

    def test_vpc_creation(self):
        # Verifica se o recurso 'aws_vpc' está presente no plano
        plan = self.tf.plan(out="plan.out")
        self.assertIn("aws_vpc.k8s_vpc", plan, "VPC resource not found in plan")

    def test_subnet_count(self):
        # Valida que o número de subnets corresponde ao esperado
        outputs = self.tf.output(json=True)
        subnets = outputs["subnet_ids"]
        self.assertEqual(len(subnets), 2, "Expected 2 subnets but found a different count")

    def tearDown(self):
        self.tf.destroy(auto_approve=True)

if __name__ == "__main__":
    unittest.main()
