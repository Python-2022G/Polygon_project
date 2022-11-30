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
        return (self.a > 0 and self.b > 0 and self.c > 0) and (self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a)
    
    def get_type(self) -> str:
        '''
        This method finds the type of the triangle.
        '''
        if is_valid == True:
            if self.a == self.b or self.b == self.c or self.a == self.c:
                return 'teng yonli'
            if self.a == self.b and self.a == self.c:
                return 'muntazam'
            if self.a != self.b and self.a != self.c and self.b != self.c:
                return 'turli tomonli'
    def perimeter(self):
        '''
        This method finds the perimeter of the triangle.

        Args:
            No
        Returns:
            int or float: return perimeter of the triangle if the triangle is valid, 0 otherwise
        '''
        if is_valid == True:
            return self.a + self.b +self.c

    def area(self):
        '''
        This method finds the area of the triangle.

        Args:
            NO
        Returns:
            int or float: return area of the triangle if the triangle is valid, 0 otherwise
        '''
        return 
