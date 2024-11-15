import unittest
from terraform import Terraform

class TestIAM(unittest.TestCase):
    def setUp(self):
        # Carrega o módulo IAM
        self.tf = Terraform(working_dir="../modules/iam")
        self.tf.init()

    def test_iam_role_exists(self):
        # Executa o Terraform Plan
        plan = self.tf.plan(out="plan.out")
        # Verifica se o recurso 'aws_iam_role' está presente no plano
        self.assertIn("aws_iam_role.eks_cluster_role", plan, "IAM Role for EKS not found in plan")

    def test_iam_role_policy(self):
        # Valida se a política de confiança inclui o EKS como principal
        outputs = self.tf.output(json=True)
        assume_role_policy = outputs["assume_role_policy"]
        self.assertIn("eks.amazonaws.com", assume_role_policy, "EKS principal not included in IAM Role Policy")

    def tearDown(self):
        self.tf.destroy(auto_approve=True)

if __name__ == "__main__":
    unittest.main()
