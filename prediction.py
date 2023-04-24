import numpy as np
import pandas as pd
from Bio import SeqIO
from scipy.special import softmax
from simpletransformers.classification import ClassificationModel

def mod_predict(fa, terminal, out, mpath = 'yingjc/BertAIP'):    
    p_ids, p_seqs = read_fasta(fa)
    
    mod = ClassificationModel(
            "bert", mpath, use_cuda = False
        )
    
    predictions, raw_outputs = mod.predict(p_seqs)    
    scores = np.array([softmax(element) for element in raw_outputs])
    scores = [h[1] for h in scores]
    
    p_df = pd.DataFrame({'SeqID': p_ids,'Probability of AIP': scores,'Prediction of AIP': predictions})
    p_df = p_df.set_index('SeqID')
    
    if terminal == 'True':
        print('\n'.join(['','Result of prediction:\n']))
        print(p_df)
        
    if out != None:        
        p_df.to_csv(out)
        print('\nThe result of prediction has been saved to '+out+'!')


def read_fasta(fasta_file):
    t_pid = []
    t_pseq = []
    for precord in SeqIO.parse(open(fasta_file), 'fasta'):
        pseq = ' '.join(list(precord.seq.lower()))
        pid = precord.id
        t_pid.append(pid)
        t_pseq.append(pseq)
    return t_pid, t_pseq

