
import datetime
from classy import Class


params1 = {
     'A_s': 2.026953425643243e-09, 
     'model': 0,
     'n_s': 0.9515497332135389, 'H0': 70.02870149861917, 'omega_b': 0.022111583189426257, 'omega_cdm': 0.12137837679711455, 'Omega_Lambda': 0.7, 'tau_reio': 0.06298803397344085, 'gauge': 'new'
}

params2 = {
     'A_s': 2.026953425643243e-09, 
     'model': 0,
     'n_s': 0.9515497332135389, 'H0': 70.02870149861917, 'omega_b': 0.022111583189426257, 'omega_cdm': 0.12137837679711455, 'Omega_Lambda': 0.7, 'tau_reio': 0.06298803397344085, 'gauge': 'new', 'modes': 's', 'output': 'mPk', 'P_k_max_h/Mpc': 1
}
params3 = {
     'A_s': 2.026953425643243e-09, 
     'model': 0,
     'n_s': 0.9515497332135389, 'H0': 70.02870149861917, 'omega_b': 0.022111583189426257, 'omega_cdm': 0.12137837679711455, 'Omega_Lambda': 0.7, 'tau_reio': 0.06298803397344085, 'gauge': 'new', 'modes': 's', 'output': 'mPk tCl lCl', 'P_k_max_h/Mpc': 1
}
params4 = {
     'A_s': 2.026953425643243e-09, 
     'model': 0,
     'n_s': 0.9515497332135389, 'H0': 70.02870149861917, 'omega_b': 0.022111583189426257, 'omega_cdm': 0.12137837679711455, 'm_ncdm': 0.061862200042787585, 'Omega_Lambda': 0.7, 'tau_reio': 0.06298803397344085, 'gauge': 'new', 'N_ncdm': 1, 'deg_ncdm': 3, 'T_ncdm': 0.71611, 'N_eff': 0.00641
}

params5 = {
     'A_s': 2.026953425643243e-09, 
     'model': 0,
     'n_s': 0.9515497332135389, 'H0': 70.02870149861917, 'omega_b': 0.022111583189426257, 'omega_cdm': 0.12137837679711455, 'm_ncdm': 0.061862200042787585, 'Omega_Lambda': 0.7, 'tau_reio': 0.06298803397344085, 'gauge': 'new', 'modes': 's', 'N_ncdm': 1, 'deg_ncdm': 3, 'T_ncdm': 0.71611, 'N_eff': 0.00641, 'output': 'mPk', 'P_k_max_h/Mpc': 1
}
params6 = {
     'A_s': 2.026953425643243e-09, 
     'model': 0,
     'n_s': 0.9515497332135389, 'H0': 70.02870149861917, 'omega_b': 0.022111583189426257, 'omega_cdm': 0.12137837679711455, 'm_ncdm': 0.061862200042787585, 'Omega_Lambda': 0.7, 'tau_reio': 0.06298803397344085, 'gauge': 'new', 'modes': 's', 'N_ncdm': 1, 'deg_ncdm': 3, 'T_ncdm': 0.71611, 'N_eff': 0.00641, 'output': 'mPk tCl lCl', 'P_k_max_h/Mpc': 1
}
params7 = {
     'A_s': 2.026953425643243e-09, 
     'model': 1,
     'n_s': 0.9515497332135389, 'H0': 70.02870149861917, 'omega_b': 0.022111583189426257, 'omega_cdm': 0.12137837679711455, 'Omega_Lambda': 0.0, 'tau_reio': 0.06298803397344085, 'gauge': 'new', 'Minfl': 1e+16
}

params8 = {
     'A_s': 2.026953425643243e-09, 
     'model': 1,
     'n_s': 0.9515497332135389, 'H0': 70.02870149861917, 'omega_b': 0.022111583189426257, 'omega_cdm': 0.12137837679711455, 'Omega_Lambda': 0.0, 'tau_reio': 0.06298803397344085, 'gauge': 'new', 'modes': 's', 'Minfl': 1e+16, 'output': 'mPk', 'P_k_max_h/Mpc': 1
}
params9 = {
     'A_s': 2.026953425643243e-09, 
     'model': 1,
     'n_s': 0.9515497332135389, 'H0': 70.02870149861917, 'omega_b': 0.022111583189426257, 'omega_cdm': 0.12137837679711455, 'Omega_Lambda': 0.0, 'tau_reio': 0.06298803397344085, 'gauge': 'new', 'modes': 's', 'Minfl': 1e+16, 'output': 'mPk tCl lCl', 'P_k_max_h/Mpc': 1
}
params10 = {
     'A_s': 2.026953425643243e-09, 
     'model': 1,
     'n_s': 0.9515497332135389, 'H0': 70.02870149861917, 'omega_b': 0.022111583189426257, 'omega_cdm': 0.12137837679711455, 'm_ncdm': 0.061862200042787585, 'Omega_Lambda': 0.0, 'tau_reio': 0.06298803397344085, 'gauge': 'new', 'N_ncdm': 1, 'deg_ncdm': 3, 'T_ncdm': 0.71611, 'N_eff': 0.00641, 'Minfl': 1e+16
}

params11 = {
     'A_s': 2.026953425643243e-09, 
     'model': 1,
     'n_s': 0.9515497332135389, 'H0': 70.02870149861917, 'omega_b': 0.022111583189426257, 'omega_cdm': 0.12137837679711455, 'm_ncdm': 0.061862200042787585, 'Omega_Lambda': 0.0, 'tau_reio': 0.06298803397344085, 'gauge': 'new', 'modes': 's', 'N_ncdm': 1, 'deg_ncdm': 3, 'T_ncdm': 0.71611, 'N_eff': 0.00641, 'Minfl': 1e+16, 'output': 'mPk', 'P_k_max_h/Mpc': 1
}
params12 = {
     'A_s': 2.026953425643243e-09, 
     'model': 1,
     'n_s': 0.9515497332135389, 'H0': 70.02870149861917, 'omega_b': 0.022111583189426257, 'omega_cdm': 0.12137837679711455, 'm_ncdm': 0.061862200042787585, 'Omega_Lambda': 0.0, 'tau_reio': 0.06298803397344085, 'gauge': 'new', 'modes': 's', 'N_ncdm': 1, 'deg_ncdm': 3, 'T_ncdm': 0.71611, 'N_eff': 0.00641, 'Minfl': 1e+16, 'output': 'mPk tCl lCl', 'P_k_max_h/Mpc': 1
}

params = [params1, params2, params3, params4, params5, params6, params7, params8, params9, params10, params11, params12];

f = open('timings.txt', 'w')

for param in params: 
	tic = datetime.datetime.now()
	for x in range(1, 10):
		cosmo = Class()
		cosmo.set(param)
		cosmo.compute()
		cosmo.struct_cleanup()
		cosmo.empty()
	toc = datetime.datetime.now()
	print(toc-tic)
	f.write('{}\n'.format(toc-tic))


