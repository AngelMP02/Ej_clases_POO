lass A: 
    def z(self): 
        return self 
 
    def y(self, t): 
        return len(t) 
 
a = A #false
y = a.z 
print(y(a)) 
aa = a() 
print(aa is a()) 
z = aa.y 
print(z(())) 
print(a().y((a,))) 
print(A.y(aa, (a,z))) 
print(aa.y((z,1,'z'))) 

#<class '__main__.A'>
#False
#0  
#1
#2
#3