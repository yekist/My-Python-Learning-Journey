import random
def a():
    answer=random.randint(1,100)
    attemptes=0
    print("这里有一个1到100之间的数字，请你猜猜是多少")
    while True:
        b=int(input("请输入你的猜测："))
        attemptes+=1
        if b<answer:
            print("太小了")
        elif b>answer:
            print("太大了")
        elif b:
            print(f"回答正确，你用了{attemptes}次猜出了数字{answer}")
            break
if __name__=="__main__":
    a()