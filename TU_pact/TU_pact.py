# Sim ul a ti o n o f d i s c r e t e model
import numpy as np
import matplotlib.pyplotasplt

# Model Parameters
a = 0.25
b = 2

# Sim ul a ti o n Parameters
Ts = 0.1
Tstop = 30
uk = 1 # Step Response
xk = 0
N = int( Tstop /Ts ) # Sim ul a ti o n l e n g t h
data = [ ]
data . append ( xk )

# Sim ul a ti o n
for k in range (N):
    xk1 = (1-a*Ts)*xk + Ts*b*uk
    xk = xk1
    data.append ( xk1 )

# Pl o t the Sim ul a ti o n R e s ul t s
t = np.arange( 0,Tstop+Ts,Ts)

plt.plot(t,data)
# Formatting the appe a r ance o f the Pl o t
plt.title('Simulation of dxdt = −ax + bu')
plt.xlabel('t[s]')
plt.ylabel('x')
plt.grid()
plt.axis([0,30,0,8])
plt.show()