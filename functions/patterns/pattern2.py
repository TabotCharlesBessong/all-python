
#  * * * * * * * * * * *
#   * * * * * * * * * *
#    * * * * * * * * *
#     * * * * * * * *
#      * * * * * * *
#       * * * * * *
#        * * * * *
#         * * * *
#          * * *
#           * *
#            *

def pattern(n):
  k = (2 * n) - 2
  for i in range(n,-1,-1): # to print n + 1 lines
    for j in range(k,0,-1):
      print(end=" ")
    k = k +1
    for j in range(0,i+1):
      print("*",end=" ")
    print("\r")

num = int(input("Enter a number for a pattern: "))
pattern(num)