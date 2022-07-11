
import numpy as np 
import matplotlib.pyplot as plt 
  
X = ['1','3','10','20','30','33','40','43','50','53','60']
Yed = [0.09, 0.16, 0.39, 0.74, 1.07, 1.17, 1.42, 1.55, 1.85, 1.92, 2.11]
Zmulti = [1.41, 1.43, 1.47, 1.50, 1.56, 1.56, 1.58, 1.56, 1.59, 1.60, 1.67]

Yver = [0.06, 0.09, 0.22, 0.41, 0.58, 0.63, 0.77, 0.84, 1.05, 1.07, 1.15]
Zver = [1.00, 1.02, 1.03, 1.03, 1.06, 1.06, 1.06, 1.03, 1.04, 1.04, 1.09]

Yagg = [0.02, 0.06, 0.16, 0.32, 0.48, 0.53, 0.64, 0.70, 0.79, 0.84, 0.95]
Zagg = [0.003, 0.008, 0.03, 0.06, 0.09, 0.09, 0.11, 0.12, 0.14, 0.15, 0.17]

X_axis = np.arange(len(X))
  
plt.bar(X_axis - 0.2, Yed, 0.4, label = 'ed25519')
plt.bar(X_axis + 0.2, Zmulti, 0.4, label = 'BLS-multi')
  
plt.xticks(X_axis, X)
plt.xlabel("f")
plt.ylabel("Performance (ms)")
plt.title("ed25519 vs BLS multi-signatures for Consensus (Cumulative)")
plt.legend()
plt.savefig('cumulative.pdf')
