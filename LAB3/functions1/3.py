heads=int(input())
legs=int(input())
def numC_numR(heads,legs):
    #x+y=heads
    #x*2+y*4=legs
    x=(legs-2*heads)//2  
    y=heads-x
    return f"Rabbits:{x} , Chikens:{y}" #记住这个syntax
    
print(numC_numR(heads,legs))






'''
print(5 // 2)  # Нәтиже: 2  (бүтін сан)
print(10 // 5) # Нәтиже: 2  (бүтін сан)
'''
