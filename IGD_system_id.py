import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('IGDdata.csv')

y_true = df.output.tolist()
u = df.input.tolist()
yk1 = y_true.copy()
yk1.pop()


#if this were going down to second order
yk2 = yk1.copy()
yk2.pop()

#if this were going down to third order
yk3 = yk2.copy()
yk3.pop()

#make sure the len(u) and len(y_true) and len(yk1) are all the same
#by eliminating any extra rows from the top

y_true.pop(0)
u.pop(0)

#if we were going down to second order
y_true.pop(0)
u.pop(0)
yk1.pop(0)


#if we were going down to third order
y_true.pop(0)
u.pop(0)
yk1.pop(0)
yk2.pop(0)


step_size = 0.1
THETA = [0,0,0,0]
ERROR = []
for count in range(len(y_true)):
    error = y_true[count] - (THETA[0]*yk1[count]  + THETA[1]*yk2[count]+ THETA[2]*yk3[count]+ THETA[3]*u[count])
    THETA = [ THETA[0] + step_size*error*yk1[count] ,THETA[1] + step_size*error*yk2[count],THETA[2] + step_size*error*yk3[count], THETA[3] + step_size*error*u[count]]
    ERROR.append(error)
    print(f"THETA is {THETA} with error of {error}")

plt.plot(ERROR)
plt.show()

















