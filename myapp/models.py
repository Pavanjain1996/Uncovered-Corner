from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=30)
    capital = models.CharField(max_length=30)
    about = models.CharField(max_length=1000)
    flag = models.CharField(max_length=15)
    cardimage = models.CharField(max_length=15,default='CardImage.jpg')
    p1name = models.CharField(max_length=30,default='')
    p1image = models.CharField(max_length=15,default='p1.jpg')
    aboutp1 = models.CharField(max_length=1000)
    p2name = models.CharField(max_length=30,default='')
    p2image = models.CharField(max_length=15,default='p2.jpg')
    aboutp2 = models.CharField(max_length=1000)
    p3name = models.CharField(max_length=30,default='')
    p3image = models.CharField(max_length=15,default='p3.jpg')
    aboutp3 = models.CharField(max_length=1000)
    p4name = models.CharField(max_length=30,default='')
    p4image = models.CharField(max_length=15,default='p4.jpg')
    aboutp4 = models.CharField(max_length=1000)
    p5name = models.CharField(max_length=30,default='')
    p5image = models.CharField(max_length=15,default='p5.jpg')
    aboutp5 = models.CharField(max_length=1000)
    p6name = models.CharField(max_length=30,default='')
    p6image = models.CharField(max_length=15,default='p6.jpg')
    aboutp6 = models.CharField(max_length=1000)
    p7name = models.CharField(max_length=30,default='')
    p7image = models.CharField(max_length=15,default='p7.jpg')
    aboutp7 = models.CharField(max_length=1000)
    p8name = models.CharField(max_length=30,default='')
    p8image = models.CharField(max_length=15,default='p8.jpg')
    aboutp8 = models.CharField(max_length=1000)
    p9name = models.CharField(max_length=20,default='')
    p9image = models.CharField(max_length=15,default='p9.jpg')
    aboutp9 = models.CharField(max_length=1000)
    p10name = models.CharField(max_length=30,default='')
    p10image = models.CharField(max_length=15,default='p10.jpg')
    aboutp10 = models.CharField(max_length=1000)
    h1image = models.CharField(max_length=30,default='h1.jpg')
    r1image = models.CharField(max_length=30,default='r1.jpg')
    h1name = models.CharField(max_length=30,default='')
    h1rating = models.CharField(max_length=30,default='')
    h1address = models.CharField(max_length=70,default='')
    h2image = models.CharField(max_length=30,default='h2.jpg')
    r2image = models.CharField(max_length=30,default='r2.jpg')
    h2name = models.CharField(max_length=30,default='')
    h2rating = models.CharField(max_length=30,default='')
    h2address = models.CharField(max_length=70,default='')
    h3image = models.CharField(max_length=30,default='h3.jpg')
    r3image = models.CharField(max_length=30,default='r3.jpg')
    h3name = models.CharField(max_length=30,default='')
    h3rating = models.CharField(max_length=30,default='')
    h3address = models.CharField(max_length=70,default='')
    h4image = models.CharField(max_length=30,default='h4.jpg')
    r4image = models.CharField(max_length=30,default='r4.jpg')
    h4name = models.CharField(max_length=30,default='')
    h4rating = models.CharField(max_length=30,default='')
    h4address = models.CharField(max_length=70,default='')
    h5image = models.CharField(max_length=30,default='h5.jpg')
    r5image = models.CharField(max_length=30,default='r5.jpg')
    h5name = models.CharField(max_length=30,default='')
    h5rating = models.CharField(max_length=30,default='')
    h5address = models.CharField(max_length=70,default='')
    
    def __str__(self):
        return str(self.id)+'. '+self.name
    
class Feedback(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30,default='')
    feedback = models.CharField(max_length=500)
    reply = models.CharField(max_length=500,default='')
    status = models.CharField(max_length=20,default='Not Resolved')

    def __str__(self):
        return str(self.id)+'. '+self.name

class Season(models.Model):
    name = models.CharField(max_length=20)
    about = models.CharField(max_length=500)
    image = models.CharField(max_length=20)

    def __str__(self):
        return str(self.id)+'. '+self.name

class Wonder(models.Model):
    name = models.CharField(max_length=20)
    about = models.CharField(max_length=500)
    image = models.CharField(max_length=20)
    country = models.CharField(max_length=40)

    def __str__(self):
        return str(self.id)+'. '+self.name
