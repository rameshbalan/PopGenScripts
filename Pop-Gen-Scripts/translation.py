#!/usr/bin/python

from flask import Flask, render_template, request

app = Flask(__name__)

codon_table_dict = {
"UUU" : "F",
"CUU" : "L",
"AUU" : "I",
"GUU" : "V",
"UUC" : "F",
"CUC" : "L",
"AUC" : "I",
"GUC" : "V",
"UUA" : "L",
"CUA" : "L",
"AUA" : "I",     
"GUA" : "V",
"UUG" : "L",
"CUG" : "L",
"AUG" : "M",
"GUG" : "V",
"UCU" : "S",
"CCU" : "P",
"ACU" : "T",
"GCU" : "A",
"UCC" : "S",
"CCC" : "P",
"ACC" : "T",
"GCC" : "A",
"UCA" : "S",
"CCA" : "P",
"ACA" : "T",
"GCA" : "A",
"UCG" : "S",
"CCG" : "P",
"ACG" : "T",
"GCG" : "A",
"UAU" : "Y",
"CAU" : "H",
"AAU" : "N",
"GAU" : "D",
"UAC" : "Y",
"CAC" : "H",
"AAC" : "N",
"GAC" : "D",
"UAA" : "Stop",
"CAA" : "Q",
"AAA" : "K",
"GAA" : "E",
"UAG" : "Stop",
"CAG" : "Q",
"AAG" : "K",
"GAG" : "E",
"UGU" : "C",
"CGU" : "R",
"AGU" : "S",
"GGU" : "G",
"UGC" : "C",
"CGC" : "R",
"AGC" : "S",
"GGC" : "G",
"UGA" : "Stop",
"CGA" : "R",
"AGA" : "R",
"GGA" : "G",
"UGG" : "W",
"CGG" : "R",
"AGG" : "R",
"GGG" : "G"
}

@app.route('/')
def student():
   return render_template('translate.html', codon = codon_table_dict)

@app.route('/translate_result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      dna = str(result['dna'])
      i=0
      protein_list = []
      for codon in dna:
         if dna[i:i+3] in codon_table_dict.keys():
            protein_list.extend(codon_table_dict[dna[i:i+3]])
            i = i + 3
      protein = "".join(protein_list)
      return render_template("translate_result.html", protein = protein, dna = dna)

if __name__ == '__main__':
   app.debug = True
   app.run(host="0.0.0.0",port=5005)
