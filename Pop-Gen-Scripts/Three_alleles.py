#!/usr/bin/python

from flask import Flask, render_template, request
import math
from scipy.stats import chisquare
app = Flask(__name__)

@app.route('/')
def student():
   return render_template('Three_alleles.html')

@app.route('/Three_alleles_result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      AA = float(result['AA'])
      AB = float(result['AB'])
      BB = float(result['BB'])
      AC = float(result['AC'])
      BC = float(result['BC'])
      CC = float(result['CC'])
      n = int(result['Popsize'])
      A = ((AA) + (AB * 0.5) + (AC * 0.5))/100
      B = ((BB) + (AB * 0.5) + (BC * 0.5))/100
      C = (1 - A - B)
      e_AA = (A*A*n)
      e_AB = (A*B*n)
      e_BB = (B*B*n)
      e_AC = (A*C*n)
      e_BC = (B*C*n)
      e_CC = (C*C*n)
      Allele_freq_dict = {'Allele Frequency of A':A,'Allele Frequency of B':B, 'Allele Frequency of C':C}
      Observed_Geno_Freq = {'Frequency of AA':AA,'Frequency of AB':AB,'Frequency of BB':BB,'Frequency of AC':AC,'Frequency of BC':BC,'Frequency of CC':CC}
      Expected_Geno_Freq = {'Frequency of AA':e_AA,'Frequency of AB':e_AB,'Frequency of BB':e_BB,'Frequency of AC':e_AC,'Frequency of BC':e_BC,'Frequency of CC':e_CC}
      return render_template("Three_alleles_result.html", allele = Allele_freq_dict, obs = Observed_Geno_Freq, exp = Expected_Geno_Freq, AA = AA, BB = BB, CC = CC)

if __name__ == '__main__':
   app.debug = True
   app.run(host="0.0.0.0",port=5005)
