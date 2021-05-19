# # 1 _________________________
# def biggle_size(arr):
#     for i in range(len(arr)):
#         if arr[i] > 0 : 
#             arr[i]= "big"
#     return arr 
# print(biggle_size([-1,5,4,-2]))           

# #2__________________________
# def count_potv(array):
#     count = 0
#     for val in array:
#         if val > 0:
#             count += 1
#     array[len(array)-1] = count
#     return array
# print([-5,-7,2,6,22])
# print(count_potv([-5,-7,2,6,22]))  
# #_____________________________________
# # 3
# def  sum_index(arr):
#      sum = 0 
#      for v in arr:
#             sum+=v   
#      return sum 
# print(sum_index([1,5,16]))          
# #____________________________
# # 4
# def averag(arr):
#     sum = 0 
#     for v in arr: 
#         sum += v 
#     return(sum/len(arr))
# print(averag([10,8,4,9]))        

# #______________________
# # # 5 
# def ret(arr):
#     #for v in arr : 
#      return(len(arr))
# print(ret([]))

# #_________________
# #6
# def min_value(arr):
#     if len(arr) == 0 :
#         return False 
#     min = arr[0]
#     for v in arr : 
#         if v  < min :
#             min = v            
#     return min 
# print(min_value([4,1,5,9,7]))      
# print(min_value([]))  
# # #________________________________


# #7

# def max_val(arr):
#     if len(arr) == 0  :
#         return False 
#     max = arr[0]
#     for v in arr : 
#      if v > max : 
#             max = v 
#     return max         
# print(max_val([4,9,10,11]))        
# #__________________________________
# #8 _________________
# def ultimat_anlyis(arr):
#     my_dic = {'sum_total':0 , 'average': 0 , 'minimum':0 , 'maximum':0}
#     for v in arr: 
#         if my_dic['minimum'] < v:
#             my_dic['minimum'] = v 
#         if my_dic['maximum'] > v :
#              my_dic['maximum'] = v 
#         my_dic['sum_total']  += v 
#         my_dic ['average'] = my_dic['sum_total'] / len(arr)
#         return my_dic
# print(ultimat_anlyis([1,3,1,2,3,0]))

# #_____________---
# #9
# def reveres(arr):
#     for i in range(0, len(arr)-1):
#         temp = arr[i]
#         arr[i] = arr[len(arr)-1-i]
#         arr[len(arr)-1-i] = temp
#     return arr
# print(reveres([1,-9,8,-5,3]))


# class user 

class 