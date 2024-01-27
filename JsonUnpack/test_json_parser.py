from json_unpack import *
import unittest


class TestJsonParser(unittest.TestCase):
    def test_deployFT(self):
        ft_test1 = DeployFT(p="prot", op=FTOp.deploy,
                            tick=b'\x01\x02\x03\x04', max=100, lim=50, dec=10)
        test_ft_deploy_json = ft_test1.to_json()
        print(test_ft_deploy_json)
        ft_test2 = ('{"p": "prot", "op": 1, "tick": "01020304",'
                    ' "max": 100, "lim": 50, "dec": 10}')
        self.assertEqual(test_ft_deploy_json, ft_test2)
        self.assertEqual(DeployFT.from_json(test_ft_deploy_json).__dict__,
                         ft_test1.__dict__)
        print(vars(DeployFT.from_json(test_ft_deploy_json)))
        print(vars(json_to_ft_object(ft_test2)))

    def test_NFT(self):
        nft_instance = NFT(
            name='My NFT',
            description='A beautiful NFT',
            image='https://example.com/nft_image.png',
            attributes={'color': 'blue', 'size': 'medium'}
        )
        json_data = nft_instance.to_json()
        print(json_data)
        nft_instance_from_json = NFT.from_json(json_data)
        self.assertEqual(nft_instance_from_json.__dict__, nft_instance.__dict__)
        print(nft_instance_from_json.__dict__)


if __name__ == '__main__':
    unittest.main()
