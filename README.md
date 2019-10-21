# Python for data analysis in Oceanography

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/LijoDXL/OceanographyWithPython/master)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/LijoDXL/OceanographyWithPython/blob/master/LICENSE)
[![Twitter URL](https://img.shields.io/twitter/url?style=social&url=https%3A%2F%2Ftwitter.com%2FLIJODXL)](https://twitter.com/LIJODXL)

## Getting started

You can run the tutorial/slide online without installing anything on your local machine by just pressing the `launch binder` icon from the top left corner.

If you wish to have a local copy instead, follow the steps below:
* download [miniconda](https://docs.conda.io/en/latest/miniconda.html) (Python 3.x 64-bit version recommended) and install it using the instructions provided [here](https://conda.io/projects/conda/en/latest/user-guide/install/index.html).  
* copy and paste the following command in your terminal to clone this repository:

```bash
git clone https://github.com/LijoDXL/OceanographyWithPython.git
```

* change to the cloned directory and create a new conda enviornment:

```bash
cd OceanographyWithPython
conda env create -f PHYoceanENV.yml
```

* you can now activate the new enviornment by typing:

```bash
conda activate PHY_OCEAN
# when done, deactivate env by
conda deactivate
```

* currently active enviorment name will be appended to the leftmost side of your command promt. More details about managing enviornment with conda can be found [here](https://docs.conda.io/projects/conda/en/latest/user-guide/getting-started.html).

* you are all set. Take Jupyter Lab for a spin by issuing the following command:

```bash
Jupyter Lab
```
