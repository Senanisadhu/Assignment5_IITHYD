import numpy as np
import matplotlib.pyplot as plt


def line_gen(A,B):
  len =10
  dim = A.shape[0]
  x_AB = np.zeros((dim,len))
  lam_1 = np.linspace(0,1,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB

#Triangle sides
r = 5

#Equation of line PR: 0.7x-y=0
#Equation of line QR: 3.73x-y-18.65=0
arr1=np.array([0.7,-1,0])
arr2=np.array([3.73,-1,-18.65])
q = (arr2[0]*arr1[2]-arr1[0]*arr2[2])/(arr1[0]*arr2[1]-arr2[0]*arr1[1])
p = (arr1[1]*arr2[2]-arr2[1]*arr1[2])/(arr1[0]*arr2[1]-arr2[0]*arr1[1])

#Coordinates of A

print(p,q)
#Triangle vertices
P = np.array([0,0])
R = np.array([p,q])
Q = np.array([r,0])

#Generating all lines
x_PR = line_gen(P,R)
x_RQ = line_gen(R,Q)
x_QP = line_gen(Q,P)

#Plotting all lines
plt.plot(x_PR[0,:],x_PR[1,:],label='$PR$')
plt.plot(x_RQ[0,:],x_RQ[1,:],label='$RQ$')
plt.plot(x_QP[0,:],x_QP[1,:],label='$QP$')

plt.plot(P[0], P[1], 'o')
plt.text(P[0] * (1 + 0.1), P[1] * (1 - 0.1) , 'P')
plt.plot(R[0], R[1], 'o')
plt.text(R[0] * (1 - 0.2), R[1] * (1) , 'R')
plt.plot(Q[0], Q[1], 'o')
plt.text(Q[0] * (1 + 0.03), Q[1] * (1 - 0.1) , 'Q')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid()
plt.axis('equal')
plt.plot()