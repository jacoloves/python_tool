import time

def main():
    past_time = 0
    sum_second = 0
    sum_minute = 0
    sum_hour = 0

    try:
        while True:
            time.sleep(1)
            past_time = past_time+1
            if past_time == 60:
                sum_minute = sum_minute+1
                past_time = 0
            
            if sum_minute == 60:
                sum_hour += sum_hour+1
                sum_minute = 0
    except KeyboardInterrupt:
        print("\n")
        print(f"{sum_hour}:{sum_minute}:{past_time}")

if __name__ == "__main__":
    main()