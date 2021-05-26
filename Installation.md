## Prepare conda/mamba

If you already work with `conda` or want to use in the future, then this section is for you.

### I already work with conda :)

If you already work with `conda` ... congratulations :)
You can use your existing installation ... preferably on a Linux or macOS system.

Please, install `mamba` in your base environment ... we will use it later.

Activate your *base* environment:
```
conda activate base
```

OR

```
source activate base
```

Install the `mamba` package:
```
conda install mamba
```

### Install conda locally (optional)

We are installing `conda` using the *miniforge* installer.


In this example we choose *Mambaforge*, which already includes `mamba`, and install in on Linux:
```
curl -L -O https://github.com/conda-forge/miniforge/releases/latest/download/Mambaforge-$(uname)-$(uname -m).sh
bash Mambaforge-$(uname)-$(uname -m).sh
```

See the *miniforge* documentation for other options:
https://github.com/conda-forge/miniforge

### Using conda on mistral (optional)

**Note**: working on mistral is quite slow ... so not recommend for this demo.

First, login to mistral.

You can use mistral post-processing nodes with your LDAP account:
```
ssh k204nnn@mistralpp.dkrz.de
```

To avoid troubles with `conda` on mistral, unload some modules:
```
module unload anaconda2 anaconda3 netcdf_c
```

Then load the latest `python` module:
```
module load python3/unstable
```

This loads the mistral system installation of `conda`.
This installation already includes `mamba`.

Activate the `base` environment:
```
source activate base
```
