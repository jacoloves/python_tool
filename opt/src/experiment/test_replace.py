from datetime import datetime

now_time = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
now_time = now_time.replace("/", "-")
now_time = now_time.replace(" ", "T")
print(now_time)