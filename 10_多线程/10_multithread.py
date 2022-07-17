# -*- coding:utf-8 -*-
# @Time : 2022/7/17 9:40 下午
# @Author : Bin Bin Xue
# @File : 10_multithread
# @Project : python_basic

'''
    10.1 线程概念
        多线程能使一个程序同时运行多个独立的线程。（共享同样的资源）
        （举例：如一个Email系统，需要一个线程接收数据，一个线程发送数据）

    10.2 创建多线程
        import thread（使用多线程模块创建多线程）
        两种创建方式：直接通过threading.Tread()创建，或通过继承threading.Thread类创建

        10.2.1 通过threading.Thread()创建
            语法：threading.Thread(group=None,target=None,name=None,args=(),kwargs={},daemon=None)
                target-目标函数（线程调用的函数）
                name-线程名
                args,kwargs-分别是要传给目标函数的参数（元组型和字典型）
                daemon-设置线程是否随主线程一起退出

        10.2.2 通过继承threading.Thread类创建（前一种能传值，这一种不能）
            创建一个类继承后，重写父类的run()方法，会在线程启动时（start）自动启动这里的函数

    10.3 主线程
        主线程就是第一个启动的线程。（daemon属性可以判断是否是主线程，默认不跟主线程一起结束）
        注意：如果当前程序有语句，则当前主程序是主线程

    10.4 阻塞线程
            在一个线程中调用另一个线程的join()，能将当前线程阻塞，直到另一个线程终止（join表示加入，
        即先让另一个线程加入运行完。
            语法：join(timeout=None)

    10.5 判断线程是否活动
        线程的其他方法：
        （1）run() - 表示线程活动的方法
        （2）start() - 启动线程
        （3）join() - 等待至线程中止
        （4）is_alive() - 判断线程是否是活动的
        （5）getName() - 返回线程名称
        （6）setName() - 设置线程名称

    10.6 线程同步
        - 数据同步问题 - 共享资源冲突，要保证同一个资源在同一时间只有一个线程在操作，其他线程排队等待
        - Python中的锁：
            threading模块提供了RLock锁（可重入锁），acquire方法上锁，release方法解锁
        - Python中的条件锁：
            threading模块提供的condition+锁（条件锁），可应对死锁问题，一般用于较为复杂的情况
                常用方法：-acquire 调用关联锁的相应方法
                                  -release 解锁
                                  -wait 使线程进入线程池等待通知
                                  -notify 通知线程池中的某个线程排队
                                  -notifyAll() 通知线程池中所有线程排队
            典型应用：生成者-消费者问题


'''

import threading
import time

print('----------线程创建测试1----------')
# def test(x,y):
#     for i in range(x,y):
#         print(i)
# 创建线程t1，给目标函数设置默认参数1、10
# thread1=threading.Thread(name='t1',target=test,args=(1,10))
# # 创建线程t2，给目标函数设置默认参数11、20
# thread2=threading.Thread(name='t2',target=test,args=(11,20))
# 启动两个线程（两个线程同时进行）
# thread1.start()
# thread2.start()

print('----------线程创建测试2----------')
# class mythread(threading.Thread):
#     def run(self):
#         for i in range(1,10):
#             print(i)
#
# thread1 = mythread()
# thread2 = mythread()
# thread1.start()
# thread2.start()

print('----------主线程测试----------')
# 当前的主线程是主程序，创建的thread1是副线程
# daemon=True会使副线程随主线程一起结束
# def test():
#     time.sleep(10)
#     for i in range(10):
#         print(i)
# thread1 = threading.Thread(target=test,daemon=False)
# thread1.start()
# print('主线程完了')

print('----------线程阻塞测试----------')
# 将主线程阻塞，先让thread1先运行
# def test():
#     time.sleep(10)
#     for i in range(5):
#         print(i)
# thread1 = threading.Thread(target=test)
# thread1.start()
# thread1.join()
# print('主线程完成了')

print('----------线程方法测试----------')
# 测试线程方法：is_alive，getName，setName，join，start
# def test():
#     time.sleep(5)
#     for i in range(5):
#         print(i)
# thread1 = threading.Thread(target=test)
# print('1.当前线程是否是活动的：', thread1.is_alive())
# thread1.start()
# print('2.当前线程是否是活动的：', thread1.is_alive())
# print('当前线程：',thread1.getName())
# print('当前线程：',thread1.setName('thread2'))
# print('当前线程：',thread1.getName())
# thread1.join()
# print('线程完毕')

print('----------RLock可重入锁测试----------')
# x = 0
# lock = threading.RLock()
# list1 = []
# class mythread(threading.Thread):
#     def run(self):
#         global x
#         lock.acquire()
#         x += 10
#         print('%s:%d' %(self.name,x))
#         lock.release()
# for i in range(5):
#     # 创建五个线程加入到列表
#     list1.append(mythread())
# for i in list1:
#     # 逐个将列表中的线程激活（线程逐个使用锁中代码）
#     i.start()

print('----------生产者消费者问题----------')
products = []
condition = threading.Condition()

class Consumer(threading.Thread):
    def consume(self):
        global condition
        global products

        condition.acquire()
        if len(products)==0:
            condition.wait()
            print('消费者提醒：没有产品去消费了')
        products.pop()
        print('消费者提醒：消费1个产品')
        print('消费者提醒：还能消费的产品数为' + str(len(products)))
        condition.notify()          #通知
        condition.release()         #解锁
    def run(self):
        for i in range(0,20):
            time.sleep(4)               #消费一个产品的时间
            self.consume()

class Producer(threading.Thread):
    def produce(self):
        global condition
        global products

        condition.acquire()         #设置条件锁
        if len(products) == 10:
            condition.wait()           #等待
            print('生产者提醒：生产者的产品数为'+str(len(products)))
            print('生产者提醒：停止生产！')
        products.append(1)
        print('生产者提醒：产品总数为：'+ str(len(products)))
        condition.notify()          #通知
        condition.release()         #解锁

    def run(self):
        for i in range(0,20):
            time.sleep(1)           #生产一个产品的时间
            self.produce()

producer = Producer()        # 生产者实例
consumer = Consumer()     # 消费者实例
producer.start()
consumer.start()
producer.join()         #阻塞
consumer.join()
