import os
import multiprocessing 
def do_this(text):
    woo(text)
def woo(text):
    print("Pro %s",text)
if __name__=="__main__":
    dd="baka"
    p=multiprocessing.Process(target=woo,args=(dd))
    p.start()
