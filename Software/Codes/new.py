from pressure_mat import *


while True:
    s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s13, s14, s15, s16 = readPressure()
   
    if s1 >= 100 or s2 >= 100 or s3 >= 100 or s4 >= 100 :
     
        print ('Pressure pad value: %s' % leg, s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s13, s14, s15, s16)

           
          
    elif s16 >= 100 or s5 >= 100 or s6 >= 100 or s7 >= 100 or s8 >= 100 or s13 >= 100 or s9 >= 100 or s10 >= 100 or s11 >= 100:
     
            
        print ('Pressure pad value: %s' % body, s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s13, s14, s15, s16)
          
           
           
    
           
    elif s12 >= 100 or s15 >= 100 or s14 >= 100:
     
        print ('Pressure pad value: %s' % head, s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s13, s14, s15, s16)

            
     
    else:
           
        print("Pressure Pad Value: %d" %  s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s13, s14, s15, s16)