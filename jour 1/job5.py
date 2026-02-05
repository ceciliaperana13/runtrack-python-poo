class point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def afficherLesPoints(self):
        print("Coordonnées du point : (",self.x,",",self.y,")")
    def afficherX(self):
        print("coordonnée x : ",self.x)
    def afficherY(self):
        print("coordonée : " , self.y)
    def changerX(self,new_x):
        self.x = new_x
    def changerY(self,new_Y):
        self.y=new_Y
                            