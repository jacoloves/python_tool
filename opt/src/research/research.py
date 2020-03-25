import os
import sys
import glob

def research():

	try:
		SEARCH_FILE_NAME = sys.argv[1]
		print(glob.glob(f'./{SEARCH_FILE_NAME}*'))

	except:
		print("Usage: research.py arg1")
		print("使用方法: research.py 検索したいファイル名")

if __name__ == "__main__":
	research()