import functions
from pprint import pprint
try:
    res = functions.read_data("winequality.csv")
    #pprint(res, width=180)
    d_w, d_r = functions.split(res)
    #pprint(d_w)
    #pprint(d_r)
except ValueError:
    print("Ocurrió un error")