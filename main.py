import functions
from pprint import pprint
try:
    res = functions.read_data("winequality.csv")
    #pprint(res, width=100)
    d_w, d_r = functions.split(res)
    #pprint(d_w)
    #pprint(d_r)
    l = functions.reduce(d_w, 'alcohol')
    #print(l)
except ValueError:
    print("Ha ocurrido la excepción ValueError")