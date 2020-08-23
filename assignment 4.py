#1.1
#1.3
class triangle:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
class area(triangle):
    def __init__(self,*args):
        super().__init__(*args)
    def get_area(self):
        s=(self.a+self.b+self.c)/2
        return (s*(s-self.a)*(s-self.b)*(s-self.c))**0.5
t = area(3.0,4.0,5.0)
print(t.get_area())

#1.2
s=str(input("enter the words seperated by comas:"))
s=s.split(",")
def largerthan(n,s):
    result=[word for word in s if len(word)>n]
    print(result)
largerthan(2,s)

#2.1
s=str(input("enter the words seperated by comas:"))
s=s.split(",")
def lengthof(s):
    result=[len(word) for word in s]
    print(result)
lengthof(s)

#2.2
s=str(input())
s=s.lower()
def vowel_or_not(s):
    if(s=='a' or s=='e' or s=='i' or s=='o' or s=='u'):
        return True
    else:
        return False
print(vowel_or_not(s))
