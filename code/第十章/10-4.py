from math import sqrt
solution = []									#顶点合集
def convexHull(points):							
   if len(points)<=3:								#少于三点
      return points
   global solution								#引用全局变量
   points.sort(key=lambda x: x[0])					#按x坐标排序
   left_most = points[0]							#最左点
   right_most = points[len(points)-1]					#最右点
   solution.extend(left_most,right_most)			#加入顶点合集
   helper(points,left_most,right_most,True)			#分治：上包
   helper(points,left_most,right_most,False)			#分治：下包
   return solution								#输出
 #helper方法，参数为：点合集，最左点，最右点，布尔值（上包为True，下包为False）
def helper(points,left_most,right_most,upBool):	
   global solution
   if len(points) <= 1:							#如果点数为一或零
     return				#注意：除第一次调用，点合集不包括最左点与最右点	
   l = lineHelper(left_most,right_most) 				#直线
   if upBool:								#如果为上包
     up = []								#在直线之上的点集合
     max_distance = 0
     max_point = ()
     for point in points:
       distance = 0-(l[0]*point[0]+l[1]*point[1]+l[2])/sqrt(l[0]*l[0] + l[1]*l[1])  #离直线的距离
       if distance >0:	
         up.append(point)
         if distance>max_distance:
             max_distance = distance					
             max_point = point
     if max_point!=():							
         solution.append(max_point)			#最远点加入顶点合集
     helper(up,left_most, max_point,True)		#递归左上包
     helper(up,max_point,right_most,True)		#递归右上包
     else:									#如果为下包
     down = []
     min_distance = 0
     min_point = ()
     for point in points:
       distance = 0-(l[0]*point[0]+l[1]*point[1]+l[2])/sqrt(l[0]*l[0] + l[1]*l[1])
       if distance <0:
         down.append(point)
         if distance<min_distance:
             min_distance = distance
             min_point = point
     if min_point!=():
         solution.append(min_point)
     helper(down,left_most,min_point,False)		#递归左下包
     helper(down,min_point,right_most,False)	#递归右下包
 
def lineHelper(point1,point2):		#传入两点，计算直线Ax+Bx+C=0，输出[A,B,C] 
   if (point1[0]-point2[0])!=0:
     m = (point1[1]-point2[1])/(point1[0]-point2[0])
     c = point1[1] - m*point1[0]
     return [m,-1,c]
   else:
     return [1, 0, point1[0]]