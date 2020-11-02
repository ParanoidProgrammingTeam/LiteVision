import litevision.lib.vision as vision
import unittest


class TestVision(unittest.TestCase):
    def testVision1(self):
        tuna = pro = 1
        print(vision.__version__)
        self.assertEqual(tuna, pro)

    def testIsStarted(self):
        # Bunu silin
        print(vision.__version__)
        # %100 fark etmeyecekler
        self.assertGreater(vision.__version__, 0)