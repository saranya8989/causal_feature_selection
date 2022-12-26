import sys
import func
import glob,os
from tqdm import tqdm
import numpy as np

script_name = sys.argv[0]
tau_min = int(sys.argv[1])    
tau_max = int(sys.argv[2])
pc_alphaa = float(sys.argv[3])
alpha_level = float(sys.argv[4])
seednum = int(sys.argv[5])

print(f"Script {script_name} was run with tmax: {tau_min}, tmin: {tau_max}, pc_alpha: {pc_alphaa}, alpha_level: {alpha_level}, seed: {seednum}")

p1="../timeseries_csv/ts_wp/"
p2="../../targets/"

tcwp2=func._process_dataset(glob.glob(p1+'*2020chanhom*')[0]).values
tcwp3=func._process_dataset(glob.glob(p1+'*2020saudel*')[0]).values
tcwp4=func._process_dataset(glob.glob(p1+'*2020molave*')[0]).values
tcwp5=func._process_dataset(glob.glob(p1+'*2020goni*')[0]).values
tcwp6=func._process_dataset(glob.glob(p1+'*2020atsani*')[0]).values
tcwp7=func._process_dataset(glob.glob(p1+'*2020vamco*')[0]).values
tcwp8=func._process_dataset(glob.glob(p1+'*2019neoguri*')[0]).values
tcwp9=func._process_dataset(glob.glob(p1+'*2019bualoi*')[0]).values
tcwp10=func._process_dataset(glob.glob(p1+'*2019halong*')[0]).values
tcwp11=func._process_dataset(glob.glob(p1+'*2019nakri*')[0]).values
tcwp12=func._process_dataset(glob.glob(p1+'*2019fengshen*')[0]).values
tcwp13=func._process_dataset(glob.glob(p1+'*2019kalmaegi*')[0]).values
tcwp14=func._process_dataset(glob.glob(p1+'*2019fungwong*')[0]).values
tcwp15=func._process_dataset(glob.glob(p1+'*2019kammuri*')[0]).values
tcwp16=func._process_dataset(glob.glob(p1+'*2018jelawat*')[0]).values
tcwp17=func._process_dataset(glob.glob(p1+'*2018maliksi*')[0]).values
tcwp18=func._process_dataset(glob.glob(p1+'*2018kongrey*')[0]).values
tcwp19=func._process_dataset(glob.glob(p1+'*2018yutu*')[0]).values
#tcwp20=func._process_dataset(glob.glob(p1+'*2017muifa*')[0]).values
tcwp21=func._process_dataset(glob.glob(p1+'*2017lan*')[0]).values
tcwp22=func._process_dataset(glob.glob(p1+'*2017haikul*')[0]).values
tcwp23=func._process_dataset(glob.glob(p1+'*2016megi*')[0]).values
tcwp24=func._process_dataset(glob.glob(p1+'*2016sarika*')[0]).values
tcwp25=func._process_dataset(glob.glob(p1+'*2016haima*')[0]).values
tcwp26=func._process_dataset(glob.glob(p1+'*2015maysak*')[0]).values
tcwp27=func._process_dataset(glob.glob(p1+'*2015koppu*')[0]).values
tcwp28=func._process_dataset(glob.glob(p1+'*2015infa*')[0]).values
tcwp29=func._process_dataset(glob.glob(p1+'*2014tapah*')[0]).values
tcwp30=func._process_dataset(glob.glob(p1+'*2014nuri*')[0]).values
tcwp31=func._process_dataset(glob.glob(p1+'*2014hagupit*')[0]).values
tcwp32=func._process_dataset(glob.glob(p1+'*2013yagi*')[0]).values
tcwp33=func._process_dataset(glob.glob(p1+'*2013fitow*')[0]).values
tcwp34=func._process_dataset(glob.glob(p1+'*2013danas*')[0]).values
tcwp35=func._process_dataset(glob.glob(p1+'*2013francisco*')[0]).values
tcwp36=func._process_dataset(glob.glob(p1+'*2013krosa*')[0]).values
tcwp37=func._process_dataset(glob.glob(p1+'*2013haiyan*')[0]).values
tcwp38=func._process_dataset(glob.glob(p1+'*2012guchol*')[0]).values
tcwp39=func._process_dataset(glob.glob(p1+'*2012gaemi*')[0]).values
tcwp40=func._process_dataset(glob.glob(p1+'*2012maria*')[0]).values
tcwp41=func._process_dataset(glob.glob(p1+'*2012sontinh*')[0]).values
tcwp42=func._process_dataset(glob.glob(p1+'*2012bopha*')[0]).values
tcwp43=func._process_dataset(glob.glob(p1+'*2011songda*')[0]).values
tcwp44=func._process_dataset(glob.glob(p1+'*2011haima*')[0]).values
tcwp45=func._process_dataset(glob.glob(p1+'*2011nalgae*')[0]).values
tcwp46=func._process_dataset(glob.glob(p1+'*2011washi*')[0]).values

ddwp={'cyclone2':tcwp2,'cyclone3':tcwp3,'cyclone4':tcwp4,'cyclone5':tcwp5,'cyclone6':tcwp6,
      'cyclone7':tcwp7, 'cyclone8':tcwp8,'cyclone9':tcwp9,'cyclone10':tcwp10,'cyclone11':tcwp11,'cyclone12':tcwp12,
      'cyclone13':tcwp13,'cyclone14':tcwp14,'cyclone15':tcwp15,'cyclone16':tcwp16,'cyclone17':tcwp17,'cyclone18':tcwp18,
      'cyclone19':tcwp19,'cyclone21':tcwp21,'cyclone22':tcwp22,'cyclone23':tcwp23,'cyclone24':tcwp24,
      'cyclone25':tcwp25,'cyclone26':tcwp26,'cyclone27':tcwp27,'cyclone28':tcwp28,'cyclone29':tcwp29,'cyclone30':tcwp30,
      'cyclone31':tcwp31,'cyclone32':tcwp32,'cyclone33':tcwp33,'cyclone34':tcwp34,'cyclone35':tcwp35,'cyclone36':tcwp36,
      'cyclone37':tcwp37,'cyclone38':tcwp38,'cyclone39':tcwp39,'cyclone40':tcwp40,'cyclone41':tcwp41,'cyclone42':tcwp42,
      'cyclone43':tcwp43,'cyclone44':tcwp44,'cyclone45':tcwp45,'cyclone46':tcwp46}

newddwp = {}
for inte,item in enumerate(ddwp.keys()):
    newddwp[inte] = ddwp[item]
    
splitsize=16
pc_type = 'run_pcstable'
var_names=func._process_dataset(glob.glob(p1+'*2020chanhom*')[0]).columns.values.tolist()
for pc_alpha in ([pc_alphaa]):#np.linspace(0.9,0.99,10)):#,0.1,0.05,0.01,1e-3,1e-4,1e-5,1e-6,1e-7,1e-8]):_
    testindex = (func.Pipeline(newddwp,pc_alpha,alpha_level,pc_type=pc_type,tau_min0=tau_min,tau_max0=tau_max,\
                          target=None,var_name=var_names,seed=seednum).random_testindex(44,splitsize))
    traindata,validdata,testdata = func.Pipeline(newddwp,pc_alpha,alpha_level,pc_type=pc_type,tau_min0=tau_min,tau_max0=tau_max,\
                                            target=None,var_name=var_names,seed=seednum).splitdata(testindex)
    result = func.Pipeline(traindata,pc_alpha,alpha_level,pc_type=pc_type,tau_min0=tau_min,tau_max0=tau_max,\
                      target=None,var_name=var_names,seed=seednum).run_tigramite(int(44-splitsize))
    var_and_lag = [result[0],result[1],result[2]]
    wpac_mlr_precip,X_precip,y_precip = func.trainMLR_target(traindata=traindata,validdata=validdata,testdata=testdata,pc_alpha=pc_alpha,\
                                                        alpha_level=alpha_level,tau_min0=tau_min,tau_max0=tau_max,target='precip',seed=seednum,var_and_lag=var_and_lag)
    wpac_mlr_pmin,X_pmin,y_pmin = func.trainMLR_target(traindata=traindata,validdata=validdata,testdata=testdata,pc_alpha=pc_alpha,\
                                                        alpha_level=alpha_level,tau_min0=tau_min,tau_max0=tau_max,target='pmin',seed=seednum,var_and_lag=var_and_lag)
    wpac_mlr_v10,X_v10,y_v10 = func.trainMLR_target(traindata=traindata,validdata=validdata,testdata=testdata,pc_alpha=pc_alpha,\
                                                        alpha_level=alpha_level,tau_min0=tau_min,tau_max0=tau_max,target='v10',seed=seednum,var_and_lag=var_and_lag)
    
    func.save_to_pickle(loc='./data/pcstablewpac_'+str(tau_min)+'-'+str(tau_max)+'_precip.obj.'+\
                   str(np.round(pc_alpha,decimals=2))+'.'+str(seednum),\
                   var={'mlr':wpac_mlr_precip,'X':X_precip,'y':y_precip})
    
    func.save_to_pickle(loc='./data/pcstablewpac_'+str(tau_min)+'-'+str(tau_max)+'_pmin.obj.'+\
                   str(np.round(pc_alpha,decimals=2))+'.'+str(seednum),\
                   var={'mlr':wpac_mlr_pmin,'X':X_pmin,'y':y_pmin})
    func.save_to_pickle(loc='./data/pcstablewpac_'+str(tau_min)+'-'+str(tau_max)+'_v10.obj.'+\
                  str(np.round(pc_alpha,decimals=2))+'.'+str(seednum),\
                   var={'mlr':wpac_mlr_v10,'X':X_v10,'y':y_v10})
    func.save_to_pickle(loc='./data/pcstablewpac_'+str(tau_min)+'-'+str(tau_max)+'_lag_and_links.'+\
                   str(np.round(pc_alpha,decimals=2))+'.'+str(seednum),var=var_and_lag)
    
print(y_pmin['test'])