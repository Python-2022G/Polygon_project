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
        if self.a < 0:
            return False
        elif self.b < 0:
            return False
        elif self.c < 0:
            return False
        return max(self.a, self.b, self.c) < self.a + self.b + self.c - max(self.a, self.b, self.c)
    
    def get_type(self) -> str:
        '''
        This method finds the type of the triangle.
        ''' 
        if self.is_valid() == True:
            if max(self.a, self.b, self.c) == min(self.a, self.b, self.c):
                return "Teng tomonli"
            if max(self.a, self.b, self.c) == self.a:
                return "Teng tomonli"
            if max(self.a, self.b, self.c) == self.b:
                return "Teng tomonli"
            if max(self.a, self.b, self.c) == self.c:
                return "Teng tomonli"
            return "Turli tomomli"
        return False
        
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
