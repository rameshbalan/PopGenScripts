#!/usr/bin/python

from flask import Flask, render_template, request
import math
#from scipy.stats import chisquare
app = Flask(__name__)

@app.route('/')
def get_freq():
	return render_template('Frequency.html')

@app.route('/Carrier_Result',methods = ['POST', 'GET'])
def result():
	if request.method == 'POST':
		result = request.form
		popsize = int(result['PopSize'])
		recessive_freq = float(result['Recessive_Freq'])
		q = math.sqrt(float(recessive_freq/popsize))
		p = float(1-q)
		freq_carriers = (2*p*q)
		num_carriers = freq_carriers * popsize
		return render_template("Carrier_Result.html", carriers = freq_carriers, num_carriers = num_carriers)

if __name__ == '__main__':
	app.debug = True
	app.run(host="0.0.0.0",port=5001)