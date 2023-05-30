def how_much_water(water, load, clothes):
    if (clothes-load) > load: return 'Too much clothes'
    elif clothes < load: return 'Not enough clothes'
    return(round(water * 1.1 ** (clothes-load), 2))
