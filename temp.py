# -*- coding: utf-8 -*-
"""
Spyder Editor
aa
ab
This is a temporary script file.
"""

class someClass(object):
    def __init__(self, friends):
        self.friends = friends
    
    def friendCircles(friends):
        # Create a hashmap of person to friends
        friendMap = {}
        friendSet = set()
        for i in range(len(friends)):
            friendMap[i] = friends[i]
            friendSet.add(i)
        
        circles = []
        
        while friendSet:
            ele = friendSet.pop()
            circleTemp = []
            
            tempSet = set()
            tempSet.add(ele)
            
            while tempSet:
                ls_friends = friendMap[ele]
                
                for j in range(len(ls_friends)):
                    if j == ele:
                        continue
                    elif ls_friends[j] == "Y":
                        circleTemp.append(j)
                        tempSet.add(j)
                if ele in tempSet:
                    tempSet.remove(ele)
            circles.append(circleTemp)
            return len(circles)   
    

        
            
lst1 = [["Y","Y","N"],["Y","Y","N"],["N","N","Y"]]        

a = someClass(lst1)
a.findMedianSortedArrays(lst1)