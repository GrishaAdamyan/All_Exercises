def quarter(xcoord, ycoord):
    if xcoord > 0 and ycoord > 0:
        print('I quarter')
    elif xcoord < 0 and ycoord > 0:
        print('II quarter')
    elif xcoord < 0 and ycoord < 0:
        print('III quarter')
    elif xcoord > 0 and ycoord < 0:
        print('IV quarter')


quarter(float(input()), float(input()))