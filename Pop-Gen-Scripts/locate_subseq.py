#!/usr/bin/python

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def student():
   return render_template('locate_dna.html')

@app.route('/locate_dna_result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      dna = str(result['dna'])
      subseq = str(result['seq'])
      length = len(subseq)
      i=0
      location = []
      for a in dna:
         if subseq == dna[i:i+length]: 
            i += 1
            location.append(i)
         else:
            i += 1

      location = "".join(str(location))
      return render_template("locate_dna_result.html", location = location, dna = dna, subseq = subseq)

if __name__ == '__main__':
   app.debug = True
   app.run(host="0.0.0.0",port=5000)
