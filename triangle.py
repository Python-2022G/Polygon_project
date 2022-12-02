from math import sqrt
class Triangle:
    def __init__(self, a:float, b:float, c:float):
        self.a = a
        self.b = b
        self.c = c

    def is_valid(self) -> bool:
        '''
        This method checks if the triangle is valid.
        
        Args: 
            No
        Returns:
            bool: True if the triangle is valid, False otherwise
        '''
        one = 0
        if self.a > 0:
            one += 1
        elif self.b > 0:
            one += 1
        elif self.c > 0:
            one += 1
        elif self.a + self.b > self.c:
            one += 1
        elif self.a + self.c > self.b:
            one += 1
        elif self.b + self.c > self.a:
            one += 1
        return one == 6
    
    def get_type(self) -> str:
        '''
        This method finds the type of the triangle.
        ''' 
        if self.is_valid() == True:
            
        return
        
    def perimeter(self):
    
        '''
        This method finds the perimeter of the triangle.

        Args:
            No
        Returns:
            int or float: return perimeter of the triangle if the triangle is valid, 0 otherwise
        '''
        return 

    def area(self):
        '''
        This method finds the area of the triangle.

        Args:
            NO
        Returns:
            int or float: return area of the triangle if the triangle is valid, 0 otherwise
        '''
        return 
