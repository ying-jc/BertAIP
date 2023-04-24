# BertAIP  
A bidirectional encoder representation from transformers-based tool for the prediction of anti-inflammatory peptides

## Installation  
Clone BertAIP by  
```
$ git clone https://github.com/ying-jc/BertAIP.git
```  
or
Download BertAIP (ZIP file), move it to a directory where the user wants it installed, and uncompress it.

## Requirements  
BertAIP is an open-source Python-based tool, which operates depending on the Python environment (Python Version ≥ 3.0). Currently, BertAIP has only been tested on the Linux system. Before running BertAIP, the user should make sure all the following packages are installed in their Python environment: click, pandas, numpy, scipy, biopython, torch, and simpletransformers. 
These packages can be easily installed using pip by
```
$ pip install -r requirements.txt
```  

## Usage  
### Options  
For details of all options, run:  
```
$ python BertAIP.py --help

Usage: BertAIP.py [OPTIONS]

  BertAIP: A BERT-based tool for the prediction of anti-inflammatory peptides

Options:
  --seq TEXT               Protein sequence file in fasta format. (Required)
  --terminal [True|False]  Output result to the terminal. [Default: True]
                           (Optional)
  --out TEXT               The name of the output file in comma-delimited text
                           format. (Optional)
  --help                   Show this message and exit.
```  

### Notes  
#### Sequence of input
The input to BertAIP can be any number of protein sequences in FASTA format. The sequence must not contain the blurred disabilities (such as "X", "Z", "B", "J", "O", "U", and "*"), and the length must be no longer than 54aa.

#### Result of output
BertAIP outputs the results to the terminal by default. The user can specify the name of the output file to save the results to a CSV file. In the results, the first column represents the sequence name, the second column represents the estimated probability of an anti-inflammatory peptide for the corresponding sequence, and the third column represents the classification result.

## An example  
All files in the commands can be found in the directory of BertAIP.  
* Locate to the example folder:
```
$ cd BertAIP/example
```
* Run the following command to predict the sequences in the example with the default settings:
```
$ python ../BertAIP.py --seq example.fasta
```

## Citation  
Ying J. et al. A bidirectional encoder representation from transformers-based method for the prediction of anti-inflammatory peptides. (Under review)
