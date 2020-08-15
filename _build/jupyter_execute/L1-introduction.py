# Aim
1. **Introduce the python ecosystem**
    * How do I run a `.py` script?
    * Where do I enter python commands?
    * What is `Python 2` and `Python 3`?
    * wait!, there is something called `Anaconda`?
    * `JupyterLab`, `Jupyter Notebooks` and reproducible research

2. **Why should I use python?**
    * Is python as easy as `Ferret`?
    * Is python as fast as `Fortran`?
    * Does python have many toolboxes like in `MATLAB`?
    * Can python read and write `netCDF` files?
    * Can python plot geographic maps and coastlines?
    * Can it handle larger than memory files (say >2 GB)?

3. **Possibilities with python**
    * Exploratory Data Analysis
    * Interactive plotting
    * Parallel processing
    * Cloud computing
---
## Python ecosystem

### Running a `.py` script
   * Activate your environment, and run the script by
     ```bash
      python your_script.py
      ```  
### Three ways to spawn a python interpreter
   * old fashioned `python` console
   * rich and colorful `ipython` console
   * `JupyterLab`
#### Starting the console
   * In terminal, type `python`
   * In terminal, type `ipython`
   * In terminal, type `jupyter lab`
#### IPython
   * Old python interface is boring and less interactive
   * `IPython` supports tab completion, syntax highlighting, documentation lookup
   * [cell magics](https://ipython.org/ipython-doc/3/interactive/magics.html) 
     like `%run`, `%debug`, `%edit` and `%bookmark` makes interactive coding easier
```{note}
More info can be found [here](https://ipython.org/ipython-doc/3/interactive/tutorial.html)
```
#### JupyterLab and Jupyter Notebook
   * [JupyterLab](https://jupyterlab.readthedocs.io/en/stable/) is an interface where you can
       * create notebooks
       * manage files and folders 
       * display images
       * start terminal
       * display csv files and much more
   * [Notebooks](https://jupyter-notebook.readthedocs.io/en/stable/notebook.html) 
      holds your code, plots and discussion in a single space
   * Notebook sharing promotes reproducible research
   * Notebooks are future  of scientific communication,
     ([Nature article](https://www.nature.com/news/interactive-notebooks-sharing-the-code-1.16261))

   * Jupyter is not limited to Python. You can run codes in
       * `Julia`
       * `Bash`
       * `R`
       * `Pyferret` and much more
````{tip}
**Additional benefits of `JupyterLab/Notebook`**
* Start jupyter in a remote computer say HPC and connect in your local browser
  ```bash
   # in remote machine type:
   jupyter lab --no-browser --ip="$HOSTNAME" --port=8888
   # in local machine type:
   ssh -N -L 8888:localhost:8888 username@remoteIP
   ```
* Open browser and type address as `localhost:8888` and press `Enter`
* No more waiting for the slow X-window forwarding to pop-up
* Easily access and view remote files
````

## Anaconda, miniconda and conda env
   * `Anaconda` and `miniconda` differs only in the number of pre-packed packages
   * `Anaconda` comes with many common-use packages (> 500 MB)
   * While `miniconda` is a lite version (<60 MB)
   * Both installs `conda`, which is the package manager
   * `Conda` helps you isolate environments, allowing you to update/install certain packages without affecting    
     other working environment.
```{attention}
* **Stay away from Python 2**
   * Avoid Python 2. It is now in *legacy* mode
   * Packages are dropping support for Python 2
   * Most scientific packages have moved to Python 3
   * Found an old code in Python 2? Use conda to create a Python 2 environment
```
## Further references
   * Rather than general python tutorials, look for scientific computing tutorials
   * Some such python lessons covering basics are:
       * <https://geo-python.github.io/site/index.html>
       * <https://scipy-lectures.org/>
       * <https://fabienmaussion.info/scientific_programming/html/00-Introduction.html>
       * <https://github.com/geoschem/GEOSChem-python-tutorial>
       * <https://unidata.github.io/online-python-training/>
       * <https://rabernat.github.io/research_computing/>
       * <http://swcarpentry.github.io/python-novice-inflammation/>
        

