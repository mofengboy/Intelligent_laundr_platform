#############################################
# File Name: setup.py						#
# Author: huawei							#
# Mail: huawei@huawei.com					#
# Created Time:  2018-12-01 00:00:00		#
#############################################


from setuptools import setup, find_packages

setup(
    name='OceanConnect_Python_SDK',															# 项目发布的名称
    version='1.1',																			# 版本号
    description='This is OceanConnect_Python_SDK',											# 简单描述
    url='https://developer.huawei.com/ict/cn/site-oceanconnect/product/doc-next',			# 包的主页（在哪下载）
    author='huawei',																		# 作者
    author_email='huawei@huawei.com',															# 作者邮箱
    packages=find_packages(),																# 包
	include_package_data = True
)