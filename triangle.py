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
        return self.a>0 and self.b>0 and self.c>0 and self.a+self.b>self.c and self.a+self.c>self.b and self.c+self.b>self.a

    
    def get_type(self) -> str:
        '''
        This method finds the type of the triangle.
        '''
        if self.is_valid():
            if self.a==self.b or self.c==self.a or self.c==self.a:
                return "Teng yonli"
            if self.a==self.b and self.c==self.a:
                return "teng tomonli"
            return "Turli tomonli"
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
        x=self.a
        y=self.b
        z=self.c
        if self.is_valid():
            p=(x+y+z)/2
            return pow(p*(p-x)*(p-y)*(p-z),1/2)
        return False
