#!/usr/bin/env python

import prediction
import click

@click.command()
@click.option('--seq', nargs=1, required=False, type=str, prompt='Sequence file name', help='Protein sequence file in fasta format. (Required)')
@click.option('--terminal', nargs=1, required=False, default='True', type=click.Choice(['True', 'False'], case_sensitive=True), help='Output result to the terminal. [Default: True] (Optional)')
@click.option('--out', nargs=1, required=False, default=None, type=str, help='The name of the output file in comma-delimited text format. (Optional)')

def run_command(seq, terminal, out):
    """BertAIP: A BERT-based tool for the prediction of anti-inflammatory peptides"""
    prediction.mod_predict(seq, terminal, out)
    print('\nWork done!')

if __name__ == '__main__':
    run_command()