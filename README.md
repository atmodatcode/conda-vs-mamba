# conda vs mamba

Material for TGIF 28.05.2021

## The snake pit

Here are the snakes we want to deal with:

* `python`: programming language
* `conda`: package manager ... made in `python`
* `mamba`: the same as `conda` ... just makes package installation faster!

### Why conda?

* A package manager which can be used as normal user (no admin rights).
* You can build your own packages ... there is a community supporting you on *conda-forge*.
* You can create environments which contain all the packages you need.
* You can use conda environments to make your projects reproducible and interoperable.

https://docs.conda.io/en/latest/

### Why mamba?

`conda` is slow when resolving dependencies from community sources like *conda-forge*.
`mamba` is a re-implementation of `conda` in `c++` to solve this issue.

https://github.com/mamba-org/mamba

## Let's try it out in a web browser!

Click on the button to run this demo with Binder:

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/atmodatcode/conda-vs-mamba/HEAD)

It takes a while...

and then a Jupyter app opens. 
On the top right, you will find the button `New`.
Please launch a Linux terminal with: `New -> Terminal`

**Note**: Binder has a timeout after 10 minutes of inactivity.



## Working with conda

### Add conda-forge to the list of available channels

*conda-forge* provides a lot of software packages that are relevant for our work.

https://conda-forge.org/

Check if you are already using it:
```
conda config --show-sources
```

If *conda-forge* is not yet part of your channels you can add it:
```
conda config --add channels conda-forge
```

### Create a new conda environment named tgif

We don't want to install in the `conda` *base* environment.
On mistral this would also not be possible because you only have read-only access
to the *base* enviromment.

So we have to create our own `conda` environment locally (default: in your *HOME* directory).

Create the *tgif* environment which has only Python 3.x included:
```
conda create --name tgif python=3
```

See what `conda` environments are available:
```
conda env list
```

Activate the *tgif* enviromment:
```
conda activate tgif
```

### Check which conda packages are available.

List all available `conda` packages in your current (*tgif*) environment:
```
conda list
```

The `cfchecker` package is not yet available. Check if it could be installed via `conda`:
```
conda search cfchecker
```

Yes, we can! It is available on the *conda-forge* channel.

### Install more packages into the tgif environment

Install the `cfchecker`:
```
conda install cfchecker
```

Apply the `cfchecker` on a single NetCDF file:
```
cfchecks /pool/data/ICON/buildbot_data/nwp/checksuite_nwp/ICON_LAM/input/lam_test_DOM01.parent.nc
```

### Compare installation with mamba and conda

Now, we want to install more packages:
```
conda install cdo magics nco iris hdf4 gdal
```

**Note**: resolving environments takes forever!

Try the same installation with mamba:
```
mamba install cdo magics nco iris hdf4 gdal
```

**Note**: resolving environments is much faster!

### Save your tgif environment

Export your enviromment to an enviromment file (default: environment.yml):
```
conda env export --name tgif --from-history|sed -e '$ d' > environment.yml
```

**Note**: we are using `sed` to remove system-dependent prefix.

**Note**: Creating the environment file with `mamba` using the `--name` option creates an incomplete entry.  

### Deactivate and remove the tgif environment

Deactivate your *tgif* environment, going back to `conda` base:
```
conda deactivate
```

Remove your *tgif* environment:
```
conda env remove --name tgif
```

Check with:
```
conda env list
```

### Create tgif environment again

Create tgif environment from `environment.yml` file (default):
```
mamba env create
```

OR

```
mamba env create -f environment.yml
```

Activate the tgif environment:
```
conda activate tgif
```

Now you have reproduced your previous tgif environment.

cdo magics .....

## Further topics

### Reproducible environments

Make your projects reproducible using *anaconda-project*:

https://anaconda-project.readthedocs.io/en/latest/

You can use it to make your Jupyter notebooks reproducible
on different operating systems (Linux, macOS, Windows) with a complete
list of all your dependent packages.
