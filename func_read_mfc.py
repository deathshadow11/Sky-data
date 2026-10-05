# coding=utf-8
#!/usr/bin/pyhton

import numpy as np
from matplotlib import pyplot as plt

def func_read_mfc(filename):

    NDET=2048

    dt=np.dtype([('version','|S20'),
                 ('no_chan',np.int32),   #quanti canali 2047
                 ('p_spec_32bit','|S4'),
                 ('specName','|S20'),    #che misura è: spettro,hg, ecc.. se è spettro ci sono zenith teorico, zenith misurato, azimuth
                 ('site','|S20'),
                 ('spectroname','|S20'),
                 ('scan_dev','|S20'),
                 ('first_line','|S80'),
                 ('elevation',np.float32),
                 ('spaeter','|S72'),
                 ('ty',np.int32),
                 ('dateAndTime','|S28'),
                 ('low_lim',np.int32),
                 ('up_lim',np.int32),
                 ('plot_low_lim',np.int32),
                 ('plot_up_lim',np.int32),
                 ('act_chno',np.int32),
                 ('noscans',np.int32),        #quante misure sono state sommate
                 ('int_time',np.float32),     #è il tempo totale della misura
                 ('latitude',np.float32),
                 ('longitude',np.float32),
                 ('no_peaks',np.int32),
                 ('no_bands',np.int32),
                 ('min_y',np.float32),
                 ('max_y',np.float32),
                 ('y_scale',np.float32),
                 ('offset_Scale',np.float32),
                 ('wavelength1',np.float32),
                 ('average',np.float32),          #valore medio dello spettro
                 ('dispersion',np.float32,(3,)),
                 ('opt_dens',np.float32),
                 ('OldFlags_mode',np.int32),
                 ('OldFlags_smooth',np.int32),
                 ('OldFlags_det_reg',np.int32),
                 ('OldFlags_Null','|S8'),
                 ('OldFlags_Ref','|S8'),
                 ('FileName','|S8'),              #nome del file attuale
                 ('backgrnd','|S8'),
                 ('gap_list',np.int32,(40,)),
                 ('comment','|S8'),
                 ('reg_no',np.int32),
                 ('p_prev_32bit','|S4'),
                 ('p_next_32bit','|S4'),
                 ('spectrum',np.float32,(NDET-1,))])

    f=np.fromfile(filename,dtype=dt)
    d=dict(zip(f.dtype.names,f[0]))
    return d
