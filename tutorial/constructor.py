class Point:
    def __init__(self,x,y):   ####construct or create a object
        self.x = x
        self.y = y
        
    def move(self):
        print("move")

    def draw(self):
        print('draw')


point = Point(112, 434)
point.x = 1
print(point.x)
print(point.y)

