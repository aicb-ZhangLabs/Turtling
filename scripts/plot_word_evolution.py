import scipy.io 
import matplotlib.pyplot as plt 
import data 
import pickle 
import numpy as np 

beta = scipy.io.loadmat('results/detm_un_K_50_Htheta_800_Optim_adam_Clip_0.0_ThetaAct_relu_Lr_0.001_Bsz_512_RhoSize_300_L_3_minDF_10_trainEmbeddings_1_divReg_2_label10_beta.mat')['values'] ## K x T x V
print('beta: ', beta.shape)

with open('scripts/data_grants_False/min_df_10/labels/timestamps.pkl', 'rb') as f:
    timelist = pickle.load(f)
print('timelist: ', timelist)
T = len(timelist)
ticks = [str(x) for x in timelist]
print('ticks: ', ticks)

## get vocab
data_file = 'scripts/data_grants_False/min_df_10/labels'
vocab, train, valid, test = data.get_data(data_file, temporal=True)
vocab_size = len(vocab)
print(vocab_size)
## plot topics 
num_words = 10
times = [20]
num_topics = 20
'''
w_lst=[]
coh_lst=[]
from palmettopy.palmetto import Palmetto
palmetto = Palmetto()


for k in range(num_topics):
    for t in times:
        gamma = beta[k, t, :]
        top_words = list(gamma.argsort()[-num_words+1:][::-1])
        topic_words = [vocab[a] for a in top_words]
        print(topic_words)
        coh_lst.append(palmetto.get_coherence(topic_words,coherence_type="ca"))
        w_lst+=top_words
        
w_set=set(w_lst)
print(len(w_set),len(w_lst))
print(np.mean(coh_lst),coh_lst)


'''
        
for k in range(num_topics):
    for t in times:
        gamma = beta[k, t, :]
        top_words = list(gamma.argsort()[-num_words+1:][::-1])
        #print(top_words)
        topic_words = [vocab[a] for a in top_words]
        print('Topic {} .. Time: {} ===> {}'.format(k, t, topic_words))

        words=topic_words[:5]
        tokens = [vocab.index(w) for w in words]
        betas = [beta[k, :, x] for x in tokens]
        for i, comp in enumerate(betas):
            plt.plot(comp, label=words[i], lw=2, linestyle='--', marker='o', markersize=4)
        plt.legend(frameon=False)
        plt.xticks(np.arange(T)[0::10],timelist[0::10])
        
        plt.savefig('plots50/{}.png'.format(k))
        plt.clf()
'''
print('Topic Climate Change...')
num_words = 10
for t in range(46):
    gamma = beta[46, t, :]
    top_words = list(gamma.argsort()[-num_words+1:][::-1])
    topic_words = [vocab[a] for a in top_words]
    print('Time: {} ===> {}'.format(t, topic_words)) 
'''

fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(17, 10), dpi=200, facecolor='w', edgecolor='k')
ax1, ax2, ax3, ax4, ax5, ax6 = axes.flatten()

ticks = [str(x) for x in timelist]
import matplotlib


for ax in axes.flatten():
    ax.spines.right.set_visible(False)
    ax.spines.top.set_visible(False)

words_1 = ['patients', 'clinical', 'treatment', 'disease', 'therapy']
tokens_1 = [vocab.index(w) for w in words_1]
betas_1 = [beta[4, :, x] for x in tokens_1]
for i, comp in enumerate(betas_1):
    ax1.plot(range(T), comp, label=words_1[i], lw=2, marker='o', markersize=1)
ax1.legend(frameon=False)
print('np.arange(T)[0::10]: ', np.arange(T)[0::10])
ax1.set_xticks(np.arange(T)[0::10])
ax1.set_xticklabels(timelist[0::10])
#ax1.set_title('Topic "studies"', fontsize=12)


words_5 = ['proposal', 'goal', 'specific', 'potential', 'development']
tokens_5 = [vocab.index(w) for w in words_5]
betas_5 = [beta[1, :, x] for x in tokens_5]
for i, comp in enumerate(betas_5):
    ax2.plot(range(T), comp, label=words_5[i], lw=2, marker='o', markersize=1)
ax2.legend(frameon=False)
ax2.set_xticks(np.arange(T)[0::10])
ax2.set_xticklabels(timelist[0::10])
#ax2.set_title('Topic "immune"', fontsize=12)


words_11 = ['protein', 'cell', 'proteins', 'cells', 'role', 'signaling']
tokens_11 = [vocab.index(w) for w in words_11]
betas_11 = [beta[5, :, x] for x in tokens_11]
for i, comp in enumerate(betas_11):
    ax3.plot(range(T), comp, label=words_11[i], lw=2, marker='o', markersize=1)
ax3.legend(frameon=False)
ax3.set_xticks(np.arange(T)[0::10])
ax3.set_xticklabels(timelist[0::10])
#ax3.set_title('Topic "methods"', fontsize=12)


words_13 = ['gene', 'genetic', 'expression', 'analysis', 'mutations']
tokens_13 = [vocab.index(w) for w in words_13]
betas_13 = [beta[10, :, x] for x in tokens_13]
for i, comp in enumerate(betas_13):
    ax4.plot(range(T), comp, label=words_13[i], lw=2, marker='o', markersize=1)
ax4.legend(frameon=False)
ax4.set_xticks(np.arange(T)[0::10])
ax4.set_xticklabels(timelist[0::10])
#ax4.set_title('Topic "cell"', fontsize=12)


words_28 = ['heart', 'bone', 'vascular', 'insulin', 'cardiac']
tokens_28 = [vocab.index(w) for w in words_28]
betas_28 = [beta[12, :, x] for x in tokens_28]
for i, comp in enumerate(betas_28):
    ax5.plot(range(T), comp, label=words_28[i], lw=2, marker='o', markersize=1)
ax5.legend(frameon=False)
ax5.set_xticks(np.arange(T)[0::10])
ax5.set_xticklabels(timelist[0::10])
#ax5.set_title('Topic "brain"', fontsize=12)


words_29 = ['health', 'risk', 'intervention', 'care', 'factors']
tokens_29 = [vocab.index(w) for w in words_29]
betas_29 = [beta[13, :, x] for x in tokens_29]
for i, comp in enumerate(betas_29):
    ax6.plot(range(T), comp, label=words_29[i], lw=2, marker='o', markersize=1)
ax6.legend(frameon=False)
ax6.set_xticks(np.arange(T)[0::10])
ax6.set_xticklabels(timelist[0::10])
#ax6.set_title('Topic "gene"', fontsize=12)
matplotlib.rcParams['axes.linewidth'] = 3
plt.savefig('word_evolution.png')
plt.show()
