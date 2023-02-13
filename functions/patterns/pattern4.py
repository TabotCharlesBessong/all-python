
#               *
#             * *
#           * * *
#         * * * *
#       * * * * *
#     * * * * * *
#   * * * * * * *
# * * * * * * * *

def pattern(n):
  k = int(((2 * n) - 2 ) * 1)
  for i in range(0,n): # to print n lines
    for j in range(0,k): # for the spaces
      print(end=" ")
    k = k - 2
    for j in range(0,i+1): # after the spaces, you need to print the 
      print("*",end=" ")
    print("\r") # move to the right

num = int(input("Enter a number for a pattern: "))
pattern(num)