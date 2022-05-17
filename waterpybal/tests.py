
import geopandas
import rasterio
import matplotlib.pyplot as plt
from shapely.geometry import Point
import pandas as pd

# Create sampling points
points = [Point(625466, 5621289), Point(626082, 5621627), Point(627116, 5621680), Point(625095, 5622358)]
gdf = geopandas.GeoDataFrame([1, 2, 3, 4], geometry=points, crs=32630)
df=pd.read_csv(r"C:\Users\Ash kan\Documents\watbalpy\csv_to_gdal_test.csv")
gdf = geopandas.GeoDataFrame(
    df, geometry=geopandas.points_from_xy(df.lon, df.lat))
gdf.head()

src = rasterio.open(r'C:\Users\Ash kan\Downloads\s2a_l2a_fishbourne.tif')
#src = rasterio.open(r"C:\Users\Ash kan\Documents\watbalpy\temp_tiff.tiff")
from rasterio.plot import show
src=src_temp
fig, ax = plt.subplots()

# transform rasterio plot to real world coords
extent=[src.bounds[0], src.bounds[2], src.bounds[1], src.bounds[3]]
ax = rasterio.plot.show(src, extent=extent, ax=ax, cmap='pink')

gdf.plot(ax=ax)

fig.show()


x = np.linspace(-4.0, 4.0, 240)
y = np.linspace(-3.0, 3.0, 180)
X, Y = np.meshgrid(x, y)
Z1 = np.exp(-2 * np.log(2) * ((X - 0.5) ** 2 + (Y - 0.5) ** 2) / 1 ** 2)
Z2 = np.exp(-3 * np.log(2) * ((X + 0.5) ** 2 + (Y + 0.5) ** 2) / 2.5 ** 2)
Z = 10.0 * (Z2 - Z1)

#netcdf
import netCDF4 as nc
#-------------------------------------
#Integrate inputs into netCDF

#create netdcf
dir=r"C:\Users\Ash kan\Documents\watbalpy\test.nc"

ds_t=nc.Dataset(dir,'w',format='NETCDF4')

#create dimensions
time=ds.createDimension("time",None) #None: unlimited dimension
lon=ds.createDimension("lon",None)
lat=ds.createDimension("lat",None)

#create variables
times=ds.createVariable( "time","f4", ("time",) )
lons=ds.createVariable( "lon","f4", ("lon",) )
lat=ds.createVariable( "lat","f4", ("lat",) )

#define lats and longs
lats[:]=np...
lons[:]=no...
times[:]=np...

#INPUTS

#create values
#Infiltration number
INF_Val=ds.createVariable( "INF_Val","f4", ("time", "lat", "lon", ) )
INF_Val.units="No_Unit"
#ETP
ETP_Val=ds.createVariable( "ETP_Val","f4", ("time", "lat", "lon", ) )
ETP_Val.units="mm"
#PRu
PRu_Val=ds.createVariable( "PRu_Val","f4", ("time", "lat", "lon", ) )
PRu_Val.units="mm"
#Prec
Prec_Val=ds.createVariable( "Prec_Val","f4", ("time", "lat", "lon", ) )
Prec_Val.units="mm"
#CN
CN_Val=ds.createVariable( "CN_Val","f4", ("time", "lat", "lon", ) )
CN_Val.units="mm"
#--------
#Append data to the variables
 
#define ETPs (calculated for each point for all time steps)
for lat_t in lats:
    for lon_t in lons:

        ETP_Val[:,lat_t,lon_t]= #output from etp function

#(calculated for all points in each time step)
for time_t in times:
    #define INFs     
    INF_Val[time_t,:,:]= #output from INF function
    
    #define PRus (t=0)       
    PRu_Val[time,:,:]= #output from PRu function
####################
#OUTPUTS

#create variables

#ETR
ETR_Val=ds.createVariable( "ETR_Val","f4", ("time", "lat", "lon", ) )
ETR_Val.units="mm"
#Def
Def_Val=ds.createVariable( "Def_Val","f4", ("time", "lat", "lon", ) )
Def_Val.units="mm"
#Rec
Rec_Val=ds.createVariable( "Rec_Val","f4", ("time", "lat", "lon", ) )
Rec_Val.units="mm"
#Ru
Ru_Val=ds.createVariable( "Ru_Val","f4", ("time", "lat", "lon", ) )
Ru_Val.units="mm"

#from here another function that will be executed after balance calculation
#--------
#Append data to the variables
for time_t in times:
    if time_t!= 0: Ru_Val=ds["Ru_Val"][time_t-1,:,:]
    else: pass #predefined Ru
    PRu_Val=ds["PRu_Val"][time_t,:,:]
    INF_Val=ds["INF_Val"][time_t,:,:]
    ETP_Val=ds["ETP_Val"][time_t,:,:]
    
    for Ru0,I1,ETP1,PRu1 in Ru_Val,INF_Val,ETP_Val,PRu_Val:
        ETR1,Def1,Ru1,Rec1=balance_calc_point(Ru0,I1,ETP1,PRu1) #calculate balance in each point
        temp_df=ETR1,Def1,Ru1,Rec1 #append to something
    
    #append to NETCDF
    for c,i in enumerate([ETR_Val,Def_Val,Ru_Val,Rec_Val]),:
        i[time_t,:,:]=temp_df[c] 











import numpy as np
lt=np.arange(40,50,1)
lt.
ln=np.arange(-110,-100,1)

a=np.random.uniform(0,100,size=(10,10))
a.shape
a
xv=np.linspace(0.5,5,10)
yv=np.linspace(0.5,5,10)
xv.reshape(-1,1)+yv
mmm=xv.reshape(-1,1)*yv
mmm.shape




import netCDF4 as nc

fn=r"C:\Users\Ash kan\Downloads\test_echam_spectral.nc"
fn=r"C:\Users\Ash kan\Documents\watbalpy\daymet_v4_daily_hi_prcp_2021.nc"

fn=r'C:\Users\Ash kan\Documents\watbalpy\waterpybal\qgis_test3.nc'
ds=nc.Dataset(fn)


import matplotlib.pyplot as plt
arr=ds["prcp"][:,10,10].data
t=ds["time"][:]
plt.plot(t,arr)


x_min=ds["x"][0].data
y_min=ds["y"][0].data
x_max=ds["x"][-1].data
y_max=ds["y"][-1].data

lon_=ds["prcp"][0,:,:]
#plt.plot(lon_)
cmap = plt.get_cmap('Spectral')
cmap.set_bad('black')
extent = [x_min , x_max, y_min , y_max]
plt.imshow(lon_,cmap=cmap,extent=extent)

xx, locs = plt.xticks()
ll = ['%.0f' % a for a in xx]
plt.xticks(xx, ll)
plt.xticks(rotation = 45) 
plt.yticks(rotation = 45) 
plt.colorbar()
plt.show()




for dim in ds.dimensions.values():
    print (dim)

for k in ds.variables.keys():
    print ("#####\n\n",k)

print (ds.__dict__)

ds["runoff"][7,10,10]

import gdal
from osgeo import ogr
import pandas as pd

#tiff to csv
ds = gdal.Open(r'Downloads\s2a_l2a_fishbourne.tif')
xyz=gdal.Translate("dem.xyz",ds)

df=pd.read_csv("dem.xyz", sep=" ",header=None)
df.columns=["x","y","value"]
df.to_csv("dem.csv",index=False)

grid_ops=gdal.GridOptions(format="GTiff")
osgeo.gdal.Grid("gdal_test.tif",gdf,grid_ops)

###############
#to get the geotransform:
gt=ds.GetGeoTransform()
gt #(624630.0, 10.0, 0.0, 5622980.0, 0.0, -10.0)
#################
ar=ds.GetRasarterBand(1).ReadAsArray()
flat=ar.flatten()


def sumup(a,b=3,c=6):
    print (a,b,c) 
    print (a+b+c)
    return  a+b+c

def subs(a,b=7,c=10):
    print (a,b,c) 
    print (a-b-c)  
    return  a-b-c

class ETP_calcs(object):

    def __init__(self):
        #"obl" defines the obligatory input arguments of each function
        self.methods_dic={
            "kimberly_penman":{"tmean":"obl", "wind":"obl", "rs":None, "rn":None, "g":0, "tmax":None, "tmin":None, "rhmax":None, "rhmin":None, "rh":None, "pressure":None, "elevation":None, "lat":None, "n":None, "nn":None, "rso":None, "a":1.35, "b":-0.35},
            "penman":{"tmean":"obl", "wind":"obl", "rs":None, "rn":None, "g":0, "tmax":None, "tmin":None, "rhmax":None, "rhmin":None, "rh":None, "pressure":None, "elevation":None, "lat":None, "n":None, "nn":None, "rso":None, "aw":2.6, "bw":0.536, "a":1.35,"b":-0.35},
            "pm_fao56":{"tmean":"obl", "wind":"obl", "rs":None, "rn":None, "g":0, "tmax":None, "tmin":None, "rhmax":None, "rhmin":None, "rh":None, "pressure":None, "elevation":None, "lat":None, "n":None, "nn":None, "rso":None, "a":1.35, "b":-0.35},
            "priestley_taylor":{"tmean":"obl", "wind":"obl", "rs":None, "rn":None, "g":0, "tmax":None, "tmin":None, "rhmax":None, "rhmin":None, "rh":None, "pressure":None, "elevation":None, "lat":None, "n":None, "nn":None, "rso":None, "a":1.35, "b":-0.35, "alpha":1.26},
            "pm":{"tmean":"obl", "wind":"obl", "rs":None, "rn":None, "g":0, "tmax":None, "tmin":None, "rhmax":None, "rhmin":None, "rh":None, "pressure":None, "elevation":None, "lat":None, "n":None, "nn":None, "rso":None, "a":1.35, "b":-0.35, "lai":None, "croph":None, "r_l":100, "r_s":70, "ra_method":1, "a_sh":1, "a_s":1, "lai_eff":1, "srs":0.0009, "co2":300},
            "thom_oliver":{"tmean":"obl", "wind":"obl", "rs":None, "rn":None, "g":0, "tmax":None, "tmin":None, "rhmax":None, "rhmin":None, "rh":None, "pressure":None, "elevation":None, "lat":None, "n":None, "nn":None, "rso":None, "aw":2.6, "bw":0.536, "a":1.35, "b":-0.35, "lai":None, "croph":None, "r_l":100, "r_s":70, "ra_method":1, "lai_eff":1, "srs":0.0009, "co2":300},
            "blaney_criddle":{"tmean":"obl", "p":"obl", "k":0.85},
            "hamon":{"tmean":"obl", "lat":"obl"},
            "linacre":{"tmean":"obl", "elevation":"obl", "lat":"obl", "tdew":None, "tmax":None, "tmin":None},
            "romanenko":{"tmean":"obl", "rh":"obl", "k":4.5},
            "abtew":{"tmean":"obl", "rs":"obl", "k":0.53},
            "fao_24":{"tmean":"obl", "wind":"obl", "rs":"obl", "rh":"obl", "pressure":None, "elevation":None, "albedo":0.23},
            "hargreaves":{"tmean":"obl", "tmax":"obl", "tmin":"obl", "lat":"obl"},
            "jensen_haise":{"tmean":"obl", "rs":None, "cr":0.025, "tx":-3, "lat":None, "method":1},
            "makkink":{"tmean":"obl", "rs":"obl", "pressure":None, "elevation":None},
            "mcguinness_bordne":{"tmean":"obl", "lat":"obl", "k":0.0147},
            "oudin":{"tmean":"obl", "lat":"obl", "k1":100, "k2":5},
            "turc":{"tmean":"obl", "rs":"obl", "rh":"obl", "k":0.31}
        }

        self.pyet_func_dic={
            "kimberly_penman":pyet.kimberly_penman,
            "penman":pyet.penman,
            "pm_fao56":pyet.pm_fao56,
            "priestley_taylor":pyet.priestley_taylor,
            "pm":pyet.pm,
            "thom_oliver":pyet.thom_oliver,
            "blaney_criddle":pyet.blaney_criddle,
            "hamon":pyet.hamon,
            "linacre":pyet.linacre,
            "romanenko":pyet.romanenko,
            "abtew":pyet.abtew,
            "fao_24":pyet.fao_24,
            "hargreaves":pyet.hargreaves,
            "jensen_haise":pyet.jensen_haise,
            "makkink":pyet.makkink,
            "mcguinness_bordne":pyet.mcguinness_bordne,
            "oudin":pyet.oudin,
            "turc":pyet.turc,
        }
        

        self.exec_etp_inps=dict()
        self.results_df=[]

    def add_ETP_method(self,method,**kwargs):

        if method in self.methods_dic:

            kwargs_=dict()

            #add the args introduced by the user
            for k,v in kwargs.items():
                if k in self.methods_dic[method]: 
                    kwargs_[k]=v
                else: print ( "argument {} not found in the list of the ETP method argument and ignored".format(k) )
            #add default values:
            for key_arg,val_arg in self.methods_dic[method].items(): 
                if key_arg not in kwargs_: kwargs_[key_arg]=val_arg

        self.exec_etp_inps[method]=kwargs_

    def exec_ETPs(self):
        for meth_name,meth_kwargs in self.exec_etp_inps.items():
            
            etp_res=self.pyet_func_dic[meth_name](**meth_kwargs)
            self.results_df.append(etp_res)
        return self.results_df
#########

a=ETP_calcs()
a.add_ETP_method(method="w",a=100,f="45",b=0)
a.add_ETP_method(method="b",a=1500,f="45",b=400)
a.exec_ETPs()




#time
import datetime as dt
yyyy=2019
mm="09"
dd="08"
date = dt.date(int(yyyy), int(mm), int(dd), 14)

#CF also specifies that we need to provide time values relative to some origin time, 
# typically since epoch (1970-01-01 00:00:00), but we will start from 2006 for consistency with Michele's example. 

#The routine below computes the time since origin using the datetime object for the last date that was printed above (2006-01-05).
# It also shifts the value by one half day so that it complies with the CF mandate that time values represent the center of the observation period.
# Other than subtracting the datetimes, these steps are just basic arithmetic.

origin = dt.date(1970, 1, 1)                  # Create origin datetime.
since_origin = (date - origin).days           # Subtract origin from date 5.
time_v = since_origin + 0.5                   # Get fractional days.
time_b = [since_origin, since_origin + 1]     # Get time_bnds.

print("time:\t\t%s\ntime_bnds:\t%s" % (time_v, time_b))



from PyQt6 import QtCore, QtWidgets

class Select_variable_window(QtWidgets.QDialog):
    def __init__(self, items, parent=None):
        super().__init__(parent)
        lay = QtWidgets.QVBoxLayout(self)

        label = QtWidgets.QLabel("Select Variable for Scatterplot:")

        self.variablelist = QtWidgets.QListWidget()
        #self.variablelist.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.variablelist.addItems(items)

        dialogbutton = QtWidgets.QDialogButtonBox()
        #dialogbutton.setOrientation(QtCore.Qt.Horizontal)
        dialogbutton.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Ok)

        lay.addWidget(label)
        lay.addWidget(self.variablelist)
        lay.addWidget(dialogbutton)

        dialogbutton.accepted.connect(self.accept)
        dialogbutton.rejected.connect(self.reject)

    def accept(self):
        self.scattervariable = [item.text() for item in self.variablelist.selectedItems()]
        super().accept() # <-- call parent method


class FirstWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        lay = QtWidgets.QVBoxLayout(self)
        button = QtWidgets.QPushButton("Open Dialog")
        button.clicked.connect(self.on_clicked)
        lay.addWidget(button)

    @QtCore.pyqtSlot()
    def on_clicked(self):
        w = Select_variable_window(["1", "2", "3", "4"])
        print (w.exec())
        print ( QtWidgets.QDialog.accepted)

        if w.exec() == 1:
            print(w.scattervariable)

if __name__ == '__main__':
    import sys
    
    app = QtWidgets.QApplication(sys.argv)
    w = FirstWidget()
    w.show()
    sys.exit(app.exec())