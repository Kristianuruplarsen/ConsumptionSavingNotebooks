Contains Jupyter Notebooks showcasing the [ConSav package](https://github.com/NumEconCopenhagen/ConsumptionSaving).

# Getting Started

The main tool in the [ConSav package](https://github.com/NumEconCopenhagen/ConsumptionSaving) is the **ModelClass** class with predefined methods for e.g. saving and loading. Each concrete model inherits these methods and then adds methods for e.g. solving and simulating. The simplest example is the canonical buffer-stock consumption model, see the [BufferStockModel notebook](https://github.com/NumEconCopenhagen/ConsumptionSavingNotebooks/blob/master/BufferStockModel/BufferStockModel.ipynb).

The [DurableConsumptioModel notebook](https://github.com/NumEconCopenhagen/ConsumptionSavingNotebooks/blob/master/DurableConsumptionModel/DurableConsumptionModel.ipynb) contains more advanced examples. Specifically, it implements the solution methods proposed in [A Guide On Solving Non-Convex Consumption-Saving Models](https://www.dropbox.com/s/dzgoo5ywmlrecbk/WP_NEGM_2020.pdf?dl=0). See also the [results notebook](https://github.com/NumEconCopenhagen/ConsumptionSavingNotebooks/blob/master/DurableConsumptionModel/A%20Guide%20On%20Solving%20Non-Convex%20Consumption-Saving%20Models.ipynb) for this paper.

To get started:

1. Install the ConSav package (requires git): ``pip install git+https://github.com/NumEconCopenhagen/ConsumptionSaving``
2. Clone or download this repository
3. Open your notebook of choice

We recommend running the notebooks in [JupyerLab](https://jupyterlab.readthedocs.io/en/stable/). A set of guides on how to install Python and JupyterLab is available [here](https://numeconcopenhagen.netlify.com/guides/).

**New to Python?** Try out this online course, [Introduction to programming and numerical analysis](https://numeconcopenhagen.netlify.com/).

# Overview
The main notebooks are:

1. **Tools/**
   * [Linear interpolation](https://github.com/NumEconCopenhagen/ConsumptionSavingNotebooks/blob/master/Tools/Linear%20interpolation.ipynb): Showcase the **linear_interp** module
   * [Optimization](https://github.com/NumEconCopenhagen/ConsumptionSavingNotebooks/blob/master/Tools/Optimization.ipynb): Showcase the **numerical optimizer** modules
   * [Upper envelope](https://github.com/NumEconCopenhagen/ConsumptionSavingNotebooks/blob/master/Tools/Upper%20envelope.ipynb): Showcase the **upperenvelope** module
1. **BufferStockModel/**
   * [BufferStockModel](https://github.com/NumEconCopenhagen/ConsumptionSavingNotebooks/blob/master/BufferStockModel/BufferStockModel.ipynb): Guide on solving and simulating the model
   * [Example with run file and C++](https://github.com/NumEconCopenhagen/ConsumptionSavingNotebooks/blob/master/BufferStockModel/Examples%20with%20run%20file%20and%20C%2B%2B.ipynb): Advanced examples
1. **DurableConsumptionModel/**
   * [DurableConsumptioModel](https://github.com/NumEconCopenhagen/ConsumptionSavingNotebooks/blob/master/DurableConsumptionModel/DurableConsumptionModel.ipynb): Guide on solving and simulating the model
   * Results for [A Guide to Solve Non-Convex Consumption-Saving Models](https://github.com/NumEconCopenhagen/ConsumptionSavingNotebooks/blob/master/DurableConsumptionModel/A%20Guide%20On%20Solving%20Non-Convex%20Consumption-Saving%20Models.ipynb) ([paper](https://www.dropbox.com/s/dzgoo5ywmlrecbk/WP_NEGM_2020.pdf?dl=0))
1. **G2EGM/**
   * Python version of the G2EGM algorithm from [A General Endogenous Grid Method for Multi-Dimensional Models with Non-Convexities and Constraints](https://linkinghub.elsevier.com/retrieve/pii/S0165188916301920), [Druedahl](http://web.econ.ku.dk/druedahl) and [Jørgensen](http://www.tjeconomics.com/), 2017, *Journal of Economic Dynamics and Control*, 74 ([MATLAB version](https://github.com/JeppeDruedahl/G2EGM))
1. **Numba and C++/**
   * [Working with Numba](https://github.com/NumEconCopenhagen/ConsumptionSavingNotebooks/blob/master/Numba%20and%20C%2B%2B/Using%20NLopt%20in%20C%2B%2B.ipynb): Simple **Numba** examples
   * [Calling C++](https://github.com/NumEconCopenhagen/ConsumptionSavingNotebooks/blob/master/Numba%20and%20C%2B%2B/Calling%20C%2B%2B.ipynb): Examples for **interfacing to C++**
   * [Using NLopt in C++](https://github.com/NumEconCopenhagen/ConsumptionSavingNotebooks/blob/master/Numba%20and%20C%2B%2B/Using%20NLopt%20in%20C%2B%2B.ipynb): Example of using the **NLopt** optimizers in C++

**Additional projects** based on **ConSav:**

* [WealthHet](https://github.com/JeppeDruedahl/WealthHet): On explaining wealth inequality.
