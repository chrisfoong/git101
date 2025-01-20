'''
day = float(input())
velocity = float(input())
'''
day = 219000.0
velocity = 83.33

#---------
day = day * 24 * 60 * 60            #second
velocity =  velocity * 1000         #metre/s
s = day * velocity                  # second * metre/second

light_year = 3 * 10**8 * 365 * 24 * 60 * 60 #metre


print(f"{s/light_year : .6f}")