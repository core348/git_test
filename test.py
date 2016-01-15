#!/usr/bin/python
#coding:utf-8

import os,sys

class Car:
    
    def __init__(self,car_name):
        self.car_name = car_name

    def Logo(self):
        return self.car_name

def main():
    print Car("Toyota").Logo()

if(__name__=="__main__"):
    main()
