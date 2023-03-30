# ***PET Calculation***

The additional variables added to the dataset in step one can be used here to calculate **evapotranspiration**.

Note that if the variable value is the same in the whole study area or it could be introduced in form of a raster (not changes in time), there is no need to add it to the dataset and the *type* field have to be *constant* or *raster*.

&nbsp;

>***IMPORTANT NOTE:*** The variable names have to be exactly the same (Case Sensitive) as it is mentioned in this guide. The WaterpyBal evapotranspiration calculation incorporate the [**pyet python library**](https://pyet.readthedocs.io/en/latest/api/index.html). To keep the consistency between pyet and WaterpyBal, the variable names are unchanged.
The units of the variables could be found [here](https://pyet.readthedocs.io/en/latest/methods/units.html).

&nbsp;

Aformentioned variables vary based on the method that is going to be used for evapotranspiration calculation. The correct method have to be selected by the user based on the ** dataset time interval**, available data, etc.

&nbsp;

### Combination evapotranspiration calculation methods:

&nbsp;


- ***Kimberly Penman:***

    tmean: **Mandatory**, wind: **Mandatory**, rs: Optional, rn: Optional, g: 0, tmax: Optional, tmin: Optional, rhmax: Optional, rhmin: Optional, rh: Optional, pressure: Optional, elevation: Optional, lat: Optional, n: Optional, nn: Optional, rso: Optional, a: 1.35, b: -0.35

- ***Penman:***
    
    tmean: **Mandatory**, wind: **Mandatory**, rs: Optional, rn: Optional, g: 0, tmax: Optional, tmin: Optional, rhmax: Optional, rhmin: Optional, rh: Optional, pressure: Optional, elevation: Optional, lat: Optional, n: Optional, nn: Optional, rso: Optional, aw: 2.6, bw: 0.536, a: 1.35,b: -0.35

- ***FAO-56 Penman-Monteith:***

    tmean: **Mandatory**, wind: **Mandatory**, rs: Optional, rn: Optional, g: 0, tmax: Optional, tmin: Optional, rhmax: Optional, rhmin: Optional, rh: Optional, pressure: Optional, elevation: Optional, lat: Optional, n: Optional, nn: Optional, rso: Optional, a: 1.35, b: -0.35

- ***Priestley and taylor:***

    tmean: **Mandatory**, wind: **Mandatory**, rs: Optional, rn: Optional, g: 0, tmax: Optional, tmin: Optional, rhmax: Optional, rhmin: Optional, rh: Optional, pressure: Optional, elevation: Optional, lat: Optional, n: Optional, nn: Optional, rso: Optional, a: 1.35, b: -0.35, alpha: 1.26

- ***Penman-Monteith:***

    tmean: **Mandatory**, wind: **Mandatory**, rs: Optional, rn: Optional, g: 0, tmax: Optional, tmin: Optional, rhmax: Optional, rhmin: Optional, rh: Optional, pressure: Optional, elevation: Optional, lat: Optional, n: Optional, nn: Optional, rso: Optional, a: 1.35, b: -0.35, lai: Optional, croph: Optional, r_l: 100, r_s: 70, ra_method: 1, a_sh: 1, a_s: 1, lai_eff: 1, srs: 0.0009, co2: 300

- ***Thom and Oliver:***

    tmean: **Mandatory**, wind: **Mandatory**, rs: Optional, rn: Optional, g: 0, tmax: Optional, tmin: Optional, rhmax: Optional, rhmin: Optional, rh: Optional, pressure: Optional, elevation: Optional, lat: Optional, n: Optional, nn: Optional, rso: Optional, aw: 2.6, bw: 0.536, a: 1.35, b: -0.35, lai: Optional, croph: Optional, r_l: 100, r_s: 70, ra_method: 1, lai_eff: 1, srs: 0.0009, co2: 300

&nbsp;

### Temperature evapotranspiration calculation methods:

&nbsp;

- ***Blaney_criddle:***

    tmean: **Mandatory**, p: **Mandatory**, k: 0.85

- ***Hamon:*** 

    tmean: **Mandatory**, lat: **Mandatory**

- ***Linacre:*** 

    tmean: **Mandatory**, elevation: **Mandatory**, lat: **Mandatory**, tdew: Optional, tmax: Optional, tmin: Optional

- ***Romanenko:*** 

    tmean: **Mandatory**, rh: **Mandatory**, k: 4.5

&nbsp;

### Radiation evapotranspiration calculation methods:

&nbsp;

- ***Abtew:*** 

    tmean: **Mandatory**, rs: **Mandatory**, k: 0.53

- ***Doorenbos–Pruitt (FAO-24):*** 

    tmean: **Mandatory**, wind: **Mandatory**, rs: **Mandatory**, rh: **Mandatory**, pressure: Optional, elevation: Optional, albedo: 0.23

- ***Hargreaves:*** 

    tmean: **Mandatory**, tmax: **Mandatory**, tmin: **Mandatory**, lat: **Mandatory**

- ***Jensen and Haise:*** 

    tmean: **Mandatory**, rs: Optional, cr: 0.025, tx: -3, lat: Optional, method: 1

- ***Makkink:*** 

    tmean: **Mandatory**, rs: **Mandatory**, pressure: Optional, elevation: Optional

- ***McGuinness and Bordne:*** 

    tmean: **Mandatory**, lat: **Mandatory**, k: 0.0147

- ***Oudin:*** 

    tmean: **Mandatory**, lat: **Mandatory**, k1: 100, k2: 5

- ***Turc:*** 

    tmean: **Mandatory**, rs: **Mandatory**, rh: **Mandatory**, k: 0.31
