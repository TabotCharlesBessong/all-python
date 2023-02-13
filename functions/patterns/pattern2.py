
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
  k = int(((2 * n) - 2 ) * 1)
  for i in range(n,-1,-1): # to print n + 1 lines
    for j in range(k,0,-1): # for the spaces
      print(end=" ")
    k = k +1
    for j in range(0,i+1): # after the spaces, you need to print the 
      print("*",end=" ")
    print("\r") # move to the right

num = int(input("Enter a number for a pattern: "))
pattern(num)