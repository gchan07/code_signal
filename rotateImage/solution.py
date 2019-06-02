'''
Note: Try to solve this task in-place (with O(1) additional memory), since this is what you'll be asked to do during an interview.

You are given an n x n 2D matrix that represents an image. Rotate the image by 90 degrees (clockwise).

Example

For

a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
the output should be

rotateImage(a) =
    [[7, 4, 1],
     [8, 5, 2],
     [9, 6, 3]]
'''


def rotateImage(a):
     list_b = []
     
     for x in range(0,len(a)):
          list_x = []
          for y in range(0, len(a[0])):
               list_x.append(a[len(a)-1-y][x])
          list_b.append(list_x)
     return list_b