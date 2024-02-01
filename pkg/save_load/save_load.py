import dill as pickle
# 假设 NFT_list, DeployFT_map, Ft_Account_map 已经正确初始化并填充了数据

save_fold = "./save/"
# 存储 NFT_list
def save_NFT_list(NFT_list):
    file_name = 'NFT_list.pkl'
    file_path = save_fold + file_name
    with open(file_path, 'wb') as file:
        pickle.dump(NFT_list, file)

# 存储 DeployFT_map
def save_DeployFT_map(DeployFT_map):
    file_name = 'DeployFT_map.pkl'
    file_path = save_fold + file_name
    with open(file_path, 'wb') as file:
        pickle.dump(DeployFT_map, file)

def save_Ft_Account_map(Ft_Account_map):
    # 存储 Ft_Account_map
    file_name = 'Ft_Account_map.pkl'
    file_path = save_fold + file_name
    with open(file_path, 'wb') as file:
        pickle.dump(Ft_Account_map, file)

# 加载 NFT_list
def load_NFT_list():
    file_name = 'NFT_list.pkl'
    file_path = save_fold + file_name
    with open(file_path, 'rb') as file:
        NFT_list = pickle.load(file)
        return NFT_list

# 加载 DeployFT_map
def load_DeployFT_map():
    file_name = 'DeployFT_map.pkl'
    file_path = save_fold + file_name
    with open(file_path, 'rb') as file:
        DeployFT_map = pickle.load(file)
        return DeployFT_map

# 加载 Ft_Account_map
def load_Ft_Account_map():
    file_name = 'Ft_Account_map.pkl'
    file_path = save_fold + file_name
    with open(file_path, 'rb') as file:
        Ft_Account_map = pickle.load(file)
        return Ft_Account_map


def save_from_block(block_num:int):
    file_name = "FROM_BLOCK.pkl"
    file_path = save_fold + file_name
    with open(file_path, 'wb') as file:
        pickle.dump(block_num, file)
    

def load_from_block():
    file_name = "FROM_BLOCK.pkl"
    file_path = save_fold + file_name
    with open(file_path, 'rb') as file:
        blocknum_hex = pickle.load(file)
        return blocknum_hex

def _int_2_hex(value):
    """
    转换整数到十六进制字符串，或十六进制字符串到整数。
    """
    if isinstance(value, int):
        # 整数转为十六进制字符串
        return hex(value)
    else:
        raise ValueError("输入类型必须是整数或十六进制字符串")
