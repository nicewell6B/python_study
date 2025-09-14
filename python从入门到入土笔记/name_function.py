'''def get_formatted_name(first, last):
    """生成格式规范的姓名"""
    full_name = f"{first} {last}"
    return full_name.title()'''
'''def get_formatted_name(first, middle, last):
    """生成格式规范的文件"""
    full_name = f"{first} {middle} {last}"
    return full_name.title()'''
def get_formatted_name(first, last, middle=''):
    """生成规范格式的姓名"""
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()