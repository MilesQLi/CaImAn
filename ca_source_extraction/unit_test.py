# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 18:47:13 2015

@author: epnevmatikakis
"""
#%%
import pims
import numpy as np
import scipy.io as sio
from greedyROI2d import greedyROI2d
from arpfit import arpfit
from sklearn.decomposition import ProjectedGradientNMF
from update_spatial_components import update_spatial_components
from update_temporal_components import update_temporal_components
from matplotlib import pyplot as plt
from time import time
from merge_rois import mergeROIS

#%% load from tiff and check they are the same with matlab
Yp =(pims.open('demoMovie.tif')) 
Y=[]
for idx,y in enumerate(Yp):
   Y.append(np.rot90(y,k=-1))

Y=np.transpose(np.array(Y),(1,2,0))
#%%
Ym = sio.loadmat('demo_results.mat')['Y']*1.0 
assert np.sum(np.abs(Y-Ym))/np.sum(np.abs(Y))==0,"Loaded movies don't match!"
#%%
#Ymat = sio.loadmat('Y.mat')
#Y = Ymat['Y']*1.

#%%
d1,d2,T = np.shape(Y)
#%% greedy initialization
nr = 30
t1 = time()
Ain,Cin,center = greedyROI2d(Y, nr = nr, gSig = [4,4], gSiz = [9,9])
t_elGREEDY = time()-t1
#%% eftychios completes here
demo_results= sio.loadmat('demo_results.mat')
Ain_m=demo_results['Ain']*1.0
Cin_m=demo_results['Cin']*1.0
center_m =demo_results['center']
if np.sum(np.abs(Ain-Ain_m))/np.sum(np.abs(Ain))!=0:    
    Ain=Ain_m
    Cin=Cin_m
    center=center_m
    raise Exception( "Greedy outputs don't match!")
#%% arpfit
active_pixels = np.squeeze(np.nonzero(np.sum(Ain,axis=1)))
Yr = np.reshape(Y,(d1*d2,T),order='F')
p = 2;
P = arpfit(Yr,p=2,pixels = active_pixels)
Y_res = Yr - np.dot(Ain,Cin)
model = ProjectedGradientNMF(n_components=1, init='random', random_state=0)
model.fit(np.maximum(Y_res,0)) 
fin = model.components_.squeeze()
#%% Eftychios completes here
demo_results= sio.loadmat('demo_results.mat', struct_as_record=False, squeeze_me=True)
Yr_m=demo_results['Yr']*1.0
P_m=demo_results['P']
fin_m =demo_results['fin']*1.0

if np.sum(np.abs(Yr-Yr_m))/np.sum(np.abs(Yr))!=0:    
    Yr=Yr_m;
    P['g']=P_m.g;
    P['sn']=P_m.sn;
    fin=fin_m
    raise Exception( "Arpfit outputs don't match!")

#%% reload all values from matlab result
demo_results= sio.loadmat('demo_results.mat',struct_as_record=False, squeeze_me=True)
Yr=demo_results['Yr']*1.0;
Cin=demo_results['Cin']*1.0
fin=demo_results['fin']*1.0
Ain=demo_results['Ain']*1.0
P_m=demo_results['P']
P=dict()
P['g']=P_m.g;
P['sn']=P_m.sn;
#%% update spatial components
t1 = time()
A,b = update_spatial_components(Yr, Cin, fin, Ain, d1=d1, d2=d2, min_size=3, max_size=8, dist=3,sn = P['sn'], method = 'ellipse')
t_elSPATIAL = time() - t1

#%% check with matlab
demo_results= sio.loadmat('demo_results.mat', struct_as_record=False, squeeze_me=True)
A_m=demo_results['A']*1.0
P_m=demo_results['P']
b_m =np.expand_dims(demo_results['b']*1.0,axis=1)
print np.sum(np.abs(A-A_m).todense())/np.sum(np.abs(A).todense()) # should give 0.0035824510737
print np.sum(np.abs(b-b_m))/np.sum(np.abs(b_m)) # should give 0.0032486662048


#%% 
t1 = time()
C,f,Y_res_temp,P_temp = update_temporal_components(Yr,A,b,Cin,fin,ITER=2,method='constrained_foopsi',deconv_method = 'cvx', g='None')
t_elTEMPORAL1 = time() - t1
#%% compare with matlab
demo_results= sio.loadmat('demo_results.mat', struct_as_record=False, squeeze_me=True)
C_m=demo_results['C']*1.0
f_m=demo_results['f']*1.0
P_temp_m=demo_results['P_temp']
Y_res_temp_m=demo_results['Y_res_temp']*1.0

#C_cor=np.squeeze(np.array([np.array(ca-pt['b'])*pt['c1'] for pt,ca in zip(P_temp,C)]))
#C_cor_m=np.squeeze(np.array([(ca-P_temp_m.b[idx])*P_temp_m.c1[idx] if np.size(P_temp_m.b[idx])>0 else ca for idx,ca in enumerate(C)]))
C_cor=np.squeeze(np.array([np.array(ca-pt['b'])for pt,ca in zip(P_temp,C)]))
C_cor_m=np.squeeze(np.array([(ca-P_temp_m.b[idx]) if np.size(P_temp_m.b[idx])>0 else ca for idx,ca in enumerate(C)]))

print np.sum(np.abs(C_cor-C_cor_m))/np.sum(np.abs(C)) # should give 0.087370193480
print np.sum(np.abs(f-f_m))/np.sum(np.abs(f)) # should give  0.0038846142374
print np.sum(np.abs(Y_res_temp-Y_res_temp_m))/np.sum(np.abs(Y_res_temp)) # 0.065985398437
pl.plot(np.sum(np.abs(C_cor-C_cor_m),axis=1))
#%%  solving using spgl1 for deconvolution
#t1 = time()
#C2,f2,Y_res2,Pnew2 = update_temporal_components(Yr,A,b,Cin,fin,ITER=2,deconv_method = 'spgl1')
#t_elTEMPORAL2 = time() - t1


#%%
t1 = time()
Am,Cm,nrm,merged_ROIs,Pm=mergeROIS(Y_res,A.tocsc(),b,np.array(C),f,d1,d2,P_new,sn=P['sn'])
t_elMERGE = time() - t1
#%% %%%%%%%%%%%%% ANDREA NEEDS TO FIX THIS %%%%%%%%%%%%%%%%%%%
##SAVE TO FILE
#np.savez('preprocess_analysis',Y_res=Y_res,A=A.todense(),b=b,C=C,f=f,d1=d1,d2=d2,P=P,Pnew=Pnew,sn=P['sn'])
#
#import numpy as np
#from scipy.sparse import csc_matrix,coo_matrix
#vars_=np.load('preprocess_analysis.npz')
#
#Y_res=vars_['Y_res']
#A=coo_matrix(vars_['A'])
#b=vars_['b']
#C=vars_['C']
#f=vars_['f']
#d1=vars_['d1']
#d2=vars_['d2']
#P=vars_['P']
#Pnew=vars_['Pnew']
#sn=vars_['sn']
##%%
#from merge_rois import mergeROIS
#A_m,C_m,nr_m,merged_ROIs,P_m=mergeROIS(Y_res,A.tocsc(),b,C,f,d1,d2,Pnew,sn=sn)