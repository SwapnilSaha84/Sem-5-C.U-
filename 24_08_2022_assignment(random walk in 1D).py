'''
Date:24_08_2022
C.U Registration No:012-1111-0753-20
C.U Roll No:203012-21-0080

Q. Random walk from origin. Draw trajectory of walker for 50 random steps. The random walk consists of 50 steps
(a)Calculate mean square displacement for 50 random steps average over 3000 independent random walk
(b)Plot the mean and mean square displacement Vs number of steps
(c)Determine slopes of two curves
(d)Calculate the probability of taking n number of steps to the right out of N number of steps
(e)Plot this probability distribution funcyion using plt.bar()
'''
import numpy as np
import matplotlib.pyplot as plt
import numpy.polynomial.polynomial as poly

N,T=3000,50#N=ensembles,T=total time steps
t=range(1,T+1)#time scale

#2D array:Time axis along row,each row is a configuration
walks=2*np.random.randint(2,size=(N,T))-1

#compute configuration average
positions=np.cumsum(walks,axis=1)
pos_sq=positions**2
mean_pos_sq=np.mean(pos_sq,axis=0)
mean_pos=np.mean(positions,axis=0)
print('The mean displacement after 50 steps',mean_pos[-1])
print('The mean square displacement after 50 steps is',mean_pos_sq[-1])

#Trajectory of walker for 50 random steps
disp=np.concatenate(([0],positions[0]))
plt.grid()
plt.title('Trajectory Of Random Walk')
plt.axvline(c='0.2')
plt.axhline(c='0.2')
plt.yticks([0,5,10,15,20,25,30,35,40,45])
plt.plot(disp,range(0,T+1))
plt.ylabel(r'Position$\longrightarrow$')
plt.xlabel(r'Step Number$\longrightarrow$')
plt.show()


#To fit
coeff_mean=poly.polyfit(t,mean_pos,1)
coeff_mean_sq=poly.polyfit(t,mean_pos_sq,1)
mean_fit=coeff_mean[1]*t+coeff_mean[0]
mean_sq_fit=coeff_mean_sq[1]*t+coeff_mean_sq[0]
#mean_fit = poly.polyval(t,coeff_mean)
#mean_sq_fit = poly.polyval(t,coeff_mean_sq)

#Plotting
plt.subplot(1,2,1)
plt.title('Mean Displacement VS Steps')
plt.plot(t,mean_pos,'o',label='mean displacement(sampled)')
plt.plot(t,mean_fit,'-',label='mean displacement(fitted)')
plt.xlabel(r'Steps$\longrightarrow$')
plt.ylabel(r'Mean Displacement $\longrightarrow$')
plt.axis([0,50,-10,10])
plt.legend(loc='best')
plt.subplot(1,2,2)
plt.title('Mean Squared Displacement VS Steps')
plt.plot(t,mean_pos_sq,'o',label='mean square displacement(sampled)')
plt.plot(t,mean_sq_fit,'-',label='mean square displacement(fitted)')
plt.xlabel(r'Steps$\longrightarrow$')
plt.ylabel(r'Mean Squared Displacement $\longrightarrow$')
plt.legend(loc='best')
plt.show()


print('Slope of mean displacement vs steps=',coeff_mean[1])
print('Slope of mean squared displacement vs steps',coeff_mean_sq[1])

S=int(input('Enter no of steps taken:',))
S_r=int(input('Enter no of steps to right:',))

def Probability_right_walk(S_r,S):
    red_walk=walks[:,:S]
    rightSteps=[np.count_nonzero(red_walk[i]==1) for i in range(N)]
    c=rightSteps.count(S_r)
    P=c*1./N
    return P
prob=np.vectorize(Probability_right_walk)
pdf=prob(t,T)


print('Probability of',S_r,'right steps out of ',S,'steps=',Probability_right_walk(S_r,S))
plt.bar(t,pdf,color='maroon')
plt.title('Probability Distribution Function')
plt.xlabel(r'Steps$\longrightarrow$')
plt.ylabel(r'Probability Distribution Function $\longrightarrow$')
plt.show()
    
    
