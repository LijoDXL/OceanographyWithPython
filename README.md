# Python for data analysis in Oceanography

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/LijoDXL/OceanographyWithPython/master)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/LijoDXL/OceanographyWithPython/blob/master/LICENSE)

[![Twitter Follow](https://img.shields.io/twitter/follow/lijodxl?style=social)](https://twitter.com/LIJODXL)

## Getting started

You can run the tutorial/slide online without installing anything on your local machine just by clicking `launch Binder` icon from the top left corner of this README file.

If you wish to have a local copy instead, follow the steps below:
* Download [miniconda](https://docs.conda.io/en/latest/miniconda.html) (Python 3.x 64-bit version recommended) and install it using the instructions provided [here](https://conda.io/projects/conda/en/latest/user-guide/install/index.html).  
* Copy and paste the following command in your terminal to clone this repository:
```bash
git clone https://github.com/LijoDXL/OceanographyWithPython.git
```
* Change to the cloned directory and create a new conda environment:
```bash
cd OceanographyWithPython
conda env create -f PHYoceanENV.yml
```
* You can now activate the new environment by typing:
```bash
conda activate PHY_OCEAN
# to deactivate env:
conda deactivate
```
* Your terminal prompt will change to indicate the currently active environment. That's it, now take JupyterLab for a spin by typing:
```bash
jupyter lab
```

## Adding packages in your environment

Suppose you want to install a new package to your PHY_OCEAN environment. Here is what you should do:
* Check the package's documentation page for a section on installation. If available, follow the instructions there. It will be usually of the form `conda install -c <channel-name> <package-name>`.
* If not, head over to [anaconda.org](https://anaconda.org/) and search with the package name there.
* From the search results, click the one with most number of downloads (conda-forge channel preferred) to find the installation step.
* Before you install, **do not forget** to activate your environment:
```bash
conda activate PHY_OCEAN
```

More details on managing environment with conda can be found [here](https://docs.conda.io/projects/conda/en/latest/user-guide/getting-started.html).

## Other tools worth learning

* [Git](https://git-scm.com): Version control your workflow. Never have the hassle of dealing with files like draft.doc,draft_edited.doc,draft_final_correction.doc,final_v1.doc,final_v2.doc,absolutely_final.doc. Learn more about git from [here](http://swcarpentry.github.io/git-novice/), [here](https://barbagroup.github.io/essential_skills_RRC/git/git/) and [here](https://www.atlassian.com/git/tutorials/comparing-workflows).

* [Tmux](https://github.com/tmux/tmux/wiki): Easily organize your various terminal sessions. Highly useful if you work with remote sessions a lot. Learn more about Tmux from [here](https://thoughtbot.com/blog/a-tmux-crash-course), [here](https://www.hamvocke.com/blog/a-quick-and-easy-guide-to-tmux/) and [here](https://tmuxp.git-pull.com/en/latest/about_tmux.html).
