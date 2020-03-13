import os
import sys

def research():
	try:
		print(sys.argv[])
	except:
		print("Usage: research.py arg1")
		print("使用方法: research.py 検索したいファイル名")

if __name__ == "__main__":
	research()