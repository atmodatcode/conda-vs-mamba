# conda-vs-mamba
Material for TGIF 28.5.21



## Installation on mistral
### To avoid troubles with conda on mistral, start with this:
```
module unload anaconda2 anaconda3 netcdf_c
module load anaconda3/bleeding_edge
```
Loads mistral system installation of conda

### Add conda-forge to the list the of available channels
conda-forge provides a lot of software packages that are relevant for our work 
  ```
conda config --add channels conda-forge
  ```
  
### Check what conda modules are available.

    List all available conda packages
  ```
  conda list
  ```
  
Check if cdo package is available
  ```
  conda list|grep cdo
  ```

Check if cfchecker package is available
  ```
  conda list|grep cfchecker
  ```

Check if cfchecker package could be installed via conda
  ```
  conda search cfchecker
  ```
Yes, we can!  BUT we cannot install it in the conda system environment.
So we have to create our own conda environment locally (default: HOME directory)
  ```
  conda search cfchecker
  ```

  
### Create a new conda environment named tgif and activate it

  ```
conda create --name tgif python=3
  ```

  ```
conda env list       # -- see what conda enviroments are available 
  ```

  ```
conda activate tgif
  ```

### Install your own packages into the tgif environment

Install the cfchecker
  ```
conda install cfchecker
  ```
Apply the cfchecker on a single NetCDF file
  ```
cfchecks /pool/data/ICON/buildbot_data/nwp/checksuite_nwp/ICON_LAM/input/lam_test_DOM01.parent.nc
  ```
  
Install mamba package manager
  ```
conda install mamba
  ```

### Compare installation with mamba and conda
  ```
conda install cdo magics nco iris hdf4 gdal  # --> resolving environments takes forever!
  ```

Try the same installation with mamba
  ```
mamba install cdo magics nco iris hdf4 gdal  # --> resolving environments is much faster!
  ```

### Save your tgif environment in an environment file (Default: environment.yml) 


  ```
conda env export --name tgif --from-history|sed -e '$ d' > environment.yml  # --> sed to remove system-dependent prefix
  ```
creating the environment file with mamba using the --name option creates an incomplete entry.  


### Deactivate and remove the tgif environment 

  ```
conda deactivate  # --> deactivates tgif, going back to conda base
  ```

  ```
conda env remove --name tgif  # --> removes tgif environment, see: conda env list
  ```

### Create tgif environment again

  ```
mamba deactivate                       # --> deactivates tgif, going back to conda base
  ```
  ```
mamba env create                       # --> creates enviromment from environment.yml (default) 
mamba env create -f environment.yml
  ```
  ```
conda activate tgif
```
now you reproduced your previous environment

cdo magics .....


