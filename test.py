from christofieds import log, log_debug

import numpy as np
import logging 

log("af")
arr = np.array([1, 2])

str_arg = []
for a in [arr, 3.4]:
    print(a)
    str_arg.append(str(a))
print(str_arg)    
logging.log(logging.DEBUG, "msg", *str_arg)

g_var = 666

def func():
    enc_var = 555

    def closure():
        print(enc_var)

        if g_var:
            print("Message")

    closure()

func()  
