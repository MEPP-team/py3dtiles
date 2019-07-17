## CityTiler quick installation notes

#### 1/ Checkout the temporary (until the ad-hoc PR gets accepted) fork [Oslandia' Py3dTiles](https://github.com/Oslandia/py3dtiles)
```
(shell) git clone https://github.com/MEPP-team/py3dtiles.git
(shell) mv py3dtiles/ py3dtiles.git
(shell) cd py3dtiles.git
(shell) git checkout Tiler
```

#### 2/ Install py3Dtiles (refer to [original install notes](docs/install.rst))
```
(shell) virtualenv -p python3 venv
(shell) source venv/bin/activate
(venv) pip install -e .
(venv) python setup.py install
(venv) pip install pytest pytest-benchmark # Optional testing
(venv) pytest                              # Optional testing
``` 
 
#### 3/ Install the tilers' specific dependency
```
(venv) pip install pyyaml
```
    
#### 4/ Configure the database description file
You can customize the [CityTilerDBConfigReference.yml](CityTilerDBConfigReference.yml) reference file:
```
(venv) pushd Tilers/CityTiler
(venv) cp CityTilerDBConfigReference.yml CityTilerDBMyConfig.yml
```
Edit `CityTilerDBMyConfig.yml` and proceed with the configuration specification
by giving the information required to access the 3DCityDB. 
Change working directory back to home of py3dtiles git clone
``` 
(venv) popd       # Refer to above pushd
``` 

#### 5a/ Running the CityTiler
From the home directory of your py3dtiles git clone, run 
```
(venv) python Tilers/CityTiler/CityTiler.py --with_BTH Tilers/CityTiler/CityTilerDBConfig.yml 
```
By default this will create a `junk` ouput directory holding the resulting tile set.


#### 5/     * in order to run the City**Temporal**Tiler you will first need to obtain the so called [evolution difference files](https://github.com/MEPP-team/RICT/tree/master/ShellScripts/computeLyonCityEvolution) between various temporal vintages. Let us assume such difference files were computed (e.g. with [computeLyonCityEvolution.sh](https://github.com/MEPP-team/RICT/blob/master/ShellScripts/computeLyonCityEvolution/computeLyonCityEvolution.sh)) in between three time stamps (2009, 20912, 2015) and for two buroughs (`LYON_1ER` and `LYON_2EME`). Then the invocation of the `CityTemporalTiler` goes 
      ```
      python Tilers/CityTiler/CityTemporalTiler.py                 \
      --db_config_path Tilers/CityTiler/CityTilerDBConfig2009.yml  \
                       Tilers/CityTiler/CityTilerDBConfig2012.yml  \
                       Tilers/CityTiler/CityTilerDBConfig2015.yml  \
      --time_stamp 2009 2012 2015                                  \
      --temporal_graph LYON_1ER_2009-2012/DifferencesAsGraph.json  \
                       LYON_1ER_2012-2015/DifferencesAsGraph.json  \
                       LYON_2EME_2009-2012/DifferencesAsGraph.json \
                       LYON_2EME_2012-2015/DifferencesAsGraph.json
      ```