import numpy as np
from sympy.solvers import solve
from sympy import Symbol
import matplotlib.pyplot as plt
import math
import scipy.misc as sc


Q = np.linspace(0.1, 0.2,10)
#Q = [0.7]
q = 1.
for q in Q:
	def PHI(x,y,z):
		#return (-q/(q+1.)/((x-1./(1.+q))**2+y**2+z**2)**0.5-1./(q+1.)/((x+1./(1.+q))**2+y**2+z**2)**0.5-0.5*(x**2+y**2))
		phi1 = -1.*q/(q+1.)/np.sqrt((x-1./(q+1.))**2+y**2+z**2)
		phi2 = -1./(q+1.)/np.sqrt((x+q/(q+1.))**2+y**2+z**2)
		phi3 = 0.5*(x**2+y**2)
		return (phi1 + phi2 - phi3)

	def PHI_X(x):
		z= 0.0
		y = 0.0
		#return (-q/(q+1.)/((x-1./(1.+q))**2+y**2+z**2)**0.5-1./(q+1.)/((x+1./(1.+q))**2+y**2+z**2)**0.5-0.5*(x**2+y**2))
		phi1 = -1.*q/(q+1.)/np.sqrt((x-1./(q+1.))**2+y**2+z**2)
		phi2 = -1./(q+1.)/np.sqrt((x+q/(q+1.))**2+y**2+z**2)
		phi3 = 0.5*(x**2+y**2)
		return (phi1 + phi2 - phi3)


	def testL(x,tabL):
		for l in tabL:
			if np.abs(l-x) < 0.1:
				return False
		return True


	tabL = []
	x = -3
	dx = 0.001
	l = 0
	while x < 3:

		if np.abs(sc.derivative(PHI_X, x,dx=0.0001))<0.01 and testL(x,tabL):# and x+0.001 not in tabL and x-0.001 not in tabL and x-0.002 not in tabL and x+0.002 not in tabL:
			#print x, sc.derivative(PHI_X, x,dx=0.0001), l
			l = l+1
			tabL.append(x)
		x = x + dx

	L2 = tabL[0]
	L1 = tabL[1]
	L3 = tabL[2]
	PHI_RL = PHI_X(L1)
	''' RYSOWANIE PUNKTOW L
	tabx = []
	taby = []
	tabc = []
	x= -2.5
	dx = 0.01
	while x < 2.5:
		tabx.append(x)
		taby.append(PHI_X(x))
		tabc.append(PHI_X(L1))
		x = x + dx
	plt.plot(tabx,taby)
	plt.plot(tabx,tabc)
	plt.ylim(-10,0)
	plt.show()
	'''




	x = L1
	y = 0.
	z = 0.
	dx = 0.005
	dy = 0.005
	dz = 0.005
	V = 0.0


	while x < L3:
		while (PHI(x,y,z) < PHI_RL):# and (PHI(x,y,z) < PHI(x,y+dy,z)): # TUTAJ sprobuj ze spadkiem phi
			while  (PHI(x,y,z) < PHI_RL):# and (PHI(x,y,z) < PHI(x,y,z+dz)): #TUTAJ
				if (PHI(x,y,z) < PHI_RL):
					V = V + dx*dy*dz
				y = y + dy
			y = 0.
			z = z + dz
		z = 0.
		y = 0.
		x = x + dx
	'''x = L3
	y = 0.
	z = 0.

	while x > L1:
		while y<0.5 and (PHI(x,y,z) < PHI_RL):#(PHI(x,y,z) < PHI_RL) and (x**2+y**2+z**2)**0.5 < max(-L2,L3):
			while z<0.5 and (PHI(x,y,z) < PHI_RL):# (PHI(x,y,z) < PHI_RL) and (x**2+y**2+z**2)**0.5 < max(-L2,L3):
				V = V + dx*dy*dz
				z = z + dz
			z = 0.
			y = y + dy
		z = 0.
		y = 0.
		x = x - dx
	'''
	print q, (3.*V/np.pi)**(1./3.)



	
	#RYSOWANIE ANIMACJI
	'''n = 1
	for z in [-0.35,-0.3,-0.25,-0.2,-0.15,-0.1,-0.05,0,0.05,0.1,0.15,0.2,0.25,0.3,0.35]:
		x = L2
		y = 0.7*L2
		dx = 0.005
		dy = 0.005

		tabx = []
		taby = []
		tabc = []

		while x < L3:
			while y < 0.7*L3:
				if PHI(x,y,z) > -7 and PHI(x,y,z)< PHI_RL:
					tabx.append(x)
					taby.append(y)
					tabc.append(PHI(x,y,z))
				y = y + dy
			y = 0.7*L2
			x = x + dx

		plt.clf()
		plt.scatter(tabx, taby, c=tabc,lw = 0)
		plt.title("q = "+str(q)+" z = "+str(z))
		plt.xlabel("x")
		plt.ylabel("y")
		plt.xlim(L2,L3)
		plt.clim(-7,PHI_RL)
		plt.ylim(0.7*L2,0.7*L3)
		plt.colorbar()
		nStr=str(n)
		nStr=nStr.rjust(5,'0')
		plt.savefig('img'+nStr+'.png')
		n = n + 1
		#plt.show()
	'''













