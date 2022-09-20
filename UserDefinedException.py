class AccessDenied(Exception):

    def __init__(self,msg):
        self.msg = msg




class AdmissionToHarward:

    def __init__(self,name,UgScore,Rank):

        self.name = name
        self.UgScore = UgScore
        self.Rank = Rank

    def check(self,confirmadmission):

        if self.UgScore < 99 and self.Rank < 10:

            raise AccessDenied(f"Sorry Sir/Madam {self.name} You Are not eligible for admission in hardward..")

        else:

            confirmadmission.content()

class AccessGranted:



    def content(self):



        print("Congratualations...!! Sir/Madam you eligible for admission in harward")


accgrt = AccessGranted()
adhrd = AdmissionToHarward("sarvesh",90,8)

try:
    adhrd.check(accgrt)

except AccessDenied as obj:
    print(obj)


