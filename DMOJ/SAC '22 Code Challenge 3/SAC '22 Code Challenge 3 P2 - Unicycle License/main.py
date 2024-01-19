speed = int(input())


quad1 = round(((5+((25-4*12*(1-speed))**0.5))/24), 6)
quad2 = round(((5-((25-4*12*(1-speed))**0.5))/24), 6)

if(quad1 >= 0):
    print(quad1)
else:
    print(quad2)