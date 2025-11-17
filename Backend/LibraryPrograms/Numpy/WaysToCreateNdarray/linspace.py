
#! <6>.linspace()
#*Syntax:    varname=numpy.linspace(start,stop,num,endpoint,retstep,dtype,axis)
#* default num = 50 and endpoint  = True
#^----------------------------------------------------------------------------------------

#& import numpy as np
# a = np.linspace(10,11)
# print(a)

# import numpy as np
# a = np.linspace(10,11,endpoint=False)
# print(a)

# import numpy as np
# a = np.linspace(10,11,retstep=True)
# print(a)
# import numpy as np
# a,rs = np.linspace(10,11,retstep=True)
# print("Content of a = ",a)
# print("return step a = ",rs)

import numpy as np
a,rs = np.linspace(10,20,num = 5,endpoint=False,retstep=True)
print(a)
print(rs)

#* Generate 10 equal samples between 10 and 11 
# import numpy as np
# a,rv = np.linspace(10,11,num = 10,retstep= True)
# print("Content of a = ",a)
# print("Return step = ",rv)

# p = 1
# for i in a:
#      # print(round(i,2))
#      print(f"%0.2f"%i)