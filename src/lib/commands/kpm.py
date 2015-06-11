# coding: utf8

def kpm(arr_data):
	sum = 0
	for i in range(0, len(arr_data['kappa_arr'])):
		sum += arr_data['kappa_arr'][i]
	return 'Current KPM: %.2f' % (float(sum)/300.0)