import sys
from sklearn.metrics import confusion_matrix
from sklearn.metrics import plot_confusion_matrix
from utils import *
from sympy import false, true
sys.path.append('../-Intelligent_Placer/intelligent_placer_lib')
import intelligent_placer
import glob
import os
imageList = sorted(glob.glob(".\Input/*.jpg"))
true_neg = 0
true_pos = 0
false_pos = 0
false_neg = 0
for one in imageList:
    bool_Check = intelligent_placer.checkImage(one)
    
    gt = False if "false" in one else True
    with open(".\Result test/result.txt", "a") as file:
      file.write("{} , Result Algoritm : {} ,Result in name : {} ,Otvet : {}  \n ".format(one ,bool_Check,gt,bool_Check == gt ))
    if(gt == False and bool_Check== False ):
      true_neg +=1
    if(gt == True and bool_Check== True ):
      true_pos += 1
    if(gt == True and bool_Check== False ):
        false_pos += 1
    if(gt == False and bool_Check== True ):
        false_neg += 1

print(true_neg , true_pos , false_neg , false_pos)

y_true = [true_neg , true_pos]
false_neg1  = [false_neg ] 
false_pos1 = [false_pos]

plot_confusion_matrix(y_true ,false_neg , false_pos )