import time

def main():
    # 経過時間測定変数（int）
    past_time = 0
    sum_minute = 0
    sum_hour = 0

    # 経過時間出力変数（str）
    str_second = ""
    str_minute = ""
    str_hour = ""

    try:
        while True:
            time.sleep(1)
            past_time = past_time+1

            # 60秒になったらmin+1をして、secを初期化
            if past_time == 60:
                sum_minute = sum_minute+1
                past_time = 0

            # 60分になったらhour+1をして、minを初期化
            if sum_minute == 60:
                sum_hour += sum_hour+1
                sum_minute = 0
 
            # きれいに00と表示させたいのでここで文字列に変換をかける
            # int second -> str second
            if (past_time < 10):
                str_second = "0"+str(past_time)
            else:
                str_second = str(past_time)

            # int minute -> str minute
            if (sum_minute < 10):
                str_minute = "0"+str(sum_minute)
            else:
                str_minute = str(sum_minute)

            # int hour -> str hour
            if (sum_hour < 10):
                str_hour = "0" + str(sum_hour)
            else:
                str_hour = str(sum_hour)

    # ctrl+cを押されたら合計時間を出力する
    except KeyboardInterrupt:
        print("\n")
        print(f"{str_hour}:{str_minute}:{str_second}")

if __name__ == "__main__":
    main()