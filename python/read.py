import os
import sys
import subprocess
import struct
import random
import numpy as np
#from scipy.stats import multivariate_normal
#from sklearn.externals import joblib

m = 20

if __name__ == "__main__":
	source_mcep_file = sys.argv[1]
	target_mcep_file = sys.argv[2];
	source_mcep = np.loadtxt(source_mcep_file)
	#t = len(source_mcep)

	fp = open(target_mcep_file, "wb")

	for t in range(len(source_mcep)):
		x_t = source_mcep[t]
		y_t = source_mcep[t]
		
		#motation
		for i in range(len(x_t)):
			if random.randint(1, 100) == 20:
				y_t[i] = 1.2*x_t[i]
			if random.randint(1, 100) == 30:
				y_t[i] = 0.8*x_t[i]


		fp.write(struct.pack('f' * (m+1), *y_t))