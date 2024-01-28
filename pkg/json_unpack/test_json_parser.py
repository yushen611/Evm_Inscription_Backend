from json_unpack import *
import unittest


class TestJsonParser(unittest.TestCase):
    def test_deployFT(self):
        ft_deploy_instance = ('{"p": "prot", "op": 1, "tick": "01020304",'
                              '"max": 100, "lim": 50, "dec": 10}')
        result: (FT | NFT | None, bool) = json_to_object(ft_deploy_instance)
        print(result[0].__dict__, result[1])
        self.assertEqual(result[1], True)

    def test_NFT(self):
        nft_instance = ('{"name":"My NFT","description":"A beautiful NFT",'
                        '"image":"https://example.com/nft_image.png",'
                        '"attributes":[{"key": "color", "value": "blue"},'
                        '{"key":"shape", "value": "circle"}]}')
        result: (FT | NFT | None, bool) = json_to_object(nft_instance)
        print(result[0].__dict__, result[1])
        self.assertEqual(result[1], True)

    def test_wrong_json(self):
        wrong_json = '{"name":"My NFT","'
        result = json_to_object(wrong_json)
        self.assertEqual(result[0], None)
        self.assertEqual(result[1], False)

    def test_wrong_nft_json(self):
        wrong_nft_json = '{ "name":"简单编程" , "url":"www.twle.cn" }'
        result = json_to_object(wrong_nft_json)
        self.assertEqual(result[0], None)
        self.assertEqual(result[1], False)

    def test_wrong_ft_transfer_json(self):
        wrong_transfer_json = ('{"p": "example","op": 3,'
                               '"tick": "010203","to": "040506"}')
        result = json_to_object(wrong_transfer_json)
        self.assertEqual(result[0], None)
        self.assertEqual(result[1], False)

    def test_hex_2_obj(self):
        result = hex_to_object("7B2270223A202270726F74222C20226F70223A"
                               "20312C20227469636B223A2022303130323033"
                               "3034222C226D6178223A203130302C20226C69"
                               "6D223A2035302C2022646563223A2031307D")
        self.assertEqual(result[1], True)
        print(result[0].__dict__)


if __name__ == '__main__':
    unittest.main()
