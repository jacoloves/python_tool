import os
import sys
import glob

def research():
	# try:
		SEARCH_FILE_NAME = sys.argv[1]
		FILE_PATH = f'./{SEARCH_FILE_NAME}_search_result.txt'
		#file = open(FILE_PATH, 'w')
		path = os.getcwd()

		test_lis = list(path.split('/'))

		sum_dir = ""

		for i in range(len(test_lis)):
			str = ''.join(test_lis[i])
			sum_dir += str
			sum_dir += "/"
			results = glob.glob(f'%s{SEARCH_FILE_NAME}*' % sum_dir)
			for str in results:
    				print(str)
			#file.write(glob.glob(f'%s{SEARCH_FILE_NAME}*' % sum_dir))
		#file.close()

	# except:
	# 	print("Usage: research.py arg1")
	# 	print("使用方法: research.py 検索したいファイル名")

if __name__ == "__main__":
	research()