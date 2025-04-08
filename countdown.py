from time import sleep

# def countdown(n):
#     while (n >= 0):
#         print(n)
#         sleep(0.5)
#         n -= 1

def countdown_recursive(n):
    if n <=0:
        print("Stop")
    else:
        print(n)
        sleep(0.5)
        countdown_recursive(n-1)

if __name__ == '__main__':
    # countdown(10)
    countdown_recursive(10)
