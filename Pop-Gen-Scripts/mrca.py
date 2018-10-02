#!/usr/bin/python

from flask import Flask, render_template, request
import pandas as pd
import collections as c
import os

app = Flask(__name__)

APP__ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route('/')
def student():
	return render_template('mrca.html')

@app.route('/mrca_result',methods = ['POST', 'GET'])
def upload():
    target = os.path.join(APP__ROOT, 'temp/')
    print(target)

    if not os.path.isdir(target):
        os.mkdir(target)

    fasta_file = request.files 
    filename = fasta_file.filename
    print(filename)
    destination = "/".join([target, filename])
    file.save(destination)
    print(destination)

def result():
	if request.method == 'POST':
		fasta_file = request.files
		nucleotide = []
		names = []
		i = 0
		with open(filename,"r") as infile:
			for line in infile:
				if line.startswith(">"):
					names.append(line.rstrip())
				if not line.startswith(">"):
					length = len(line)
					nucleotide_list = tuple(line.rstrip())
					nucleotide.append((nucleotide_list))
			seq_df = pd.DataFrame(nucleotide,index=names)
			con_seq_df = pd.DataFrame(index=["A","C","G","T"])
			for i in range(0,length):
				a = c.Counter(seq_df.iloc[:,i])
				con_seq_df.loc["A",i] = a['A']
				con_seq_df.loc["T",i] = a['T']
				con_seq_df.loc["G",i] = a['G']
				con_seq_df.loc["C",i] = a['C']
			i = 0
			v = []
			consenus_sequence = []
			for i in range(0,length):
				v.append(con_seq_df.index[con_seq_df.iloc[:,i] == con_seq_df.iloc[:,i].max()].tolist())
			for value in v:
				consenus_sequence.append(value[0])
			con_seq = "".join(consenus_sequence)
		return render_template("mrca_result.html", con = con_seq, table = con_seq_df.to_html())

if __name__ == '__main__':
	app.debug = True
	app.run(host="0.0.0.0",port=5000)
