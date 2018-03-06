#!/usr/bin/python

from flask import Flask, render_template, request
import math
from scipy.stats import chisquare
app = Flask(__name__)

@app.route('/')
def student():
    n = 1
    Sequence = []
    return render_template('Sequence.html')

@app.route('/Sequence_result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
       result = request.form
       seq1 = str(result['seq1'])
       seq2 = str(result['seq2'])
       seq3 = str(result['seq3'])
       seq4 = str(result['seq4'])
       seq5 = str(result['seq5'])
       n = len(seq1)
       c = ((n * (n-1))/2)
       i = 0
       diff_1_2 = 0
       for nucleotide in seq1:
           if seq1[i] != seq2[i]:
               diff_1_2 += 1
           i += 1
       i = 0
       diff_1_3 = 0
       for nucleotide in seq1:
           if seq1[i] != seq3[i]:
               diff_1_3 += 1
           i += 1
       i = 0
       diff_1_4 = 0
       for nucleotide in seq1:
           if seq1[i] != seq4[i]:
               diff_1_4 += 1
           i += 1
       i = 0
       diff_1_5 = 0
       for nucleotide in seq1:
           if seq1[i] != seq5[i]:
               diff_1_5 += 1
           i += 1
       i = 0
       diff_2_3 = 0
       for nucleotide in seq2:
           if seq2[i] != seq3[i]:
               diff_2_3 += 1
           i += 1
       i = 0
       diff_2_4 = 0
       for nucleotide in seq2:
           if seq2[i] != seq4[i]:
               diff_2_4 += 1
           i += 1
       i = 0
       diff_2_5 = 0
       for nucleotide in seq2:
           if seq2[i] != seq5[i]:
               diff_2_5 += 1
           i += 1
       i = 0
       diff_3_4 = 0
       for nucleotide in seq3:
           if seq3[i] != seq4[i]:
               diff_3_4 += 1
           i += 1
       i = 0
       diff_3_5 = 0
       for nucleotide in seq3:
           if seq3[i] != seq5[i]:
               diff_3_5 += 1
           i += 1
       i = 0
       diff_4_5 = 0
       for nucleotide in seq4:
           if seq4[i] != seq5[i]:
               diff_4_5 += 1
           i += 1
       diff_list = [diff_1_2,diff_1_3,diff_1_4,diff_1_5,diff_2_3,diff_2_4,diff_2_5,diff_3_4,diff_3_5,diff_4_5]
       dij = sum(diff_list)
       pi = float(dij)/c
       return render_template("Sequence_result.html", pi = pi,dij=dij, c = c)

if __name__ == '__main__':
   app.run(debug = True)
