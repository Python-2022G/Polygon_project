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
        return (a > 0 and b > 0 and c > 0) and (a + b > c and a + c > b and b + c > a)
    
    def get_type(self) -> str:
        '''
        This method finds the type of the triangle.
        '''
        if a == b or b == c or a == c:
            return 'teng yonli'
        if a == b and a == c:
            return 'muntazam'
        if a != b and a != c and b != c:
            return 'turli tomonli'
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
