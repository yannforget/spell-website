---
author: "Marie-Cécile Dupas"
date: 2024-10-18T09:00:00+02:00
title: "New study on modelling farm distribution now published in PLoS Computational Biology"
---
Our new study on modelling farm distribution has been published in *PLoS Computational Biology*. We have developed a model to predict the location and size of poultry farms in countries or regions with limited data. This is important because knowing the distribution of farms helps in understanding how diseases spread, especially in areas with rapidly growing farm populations. Our model uses advanced statistical methods and is calibrated with environmental and human activity data to simulate farm locations and sizes, which we tested on farms in Bangladesh, Gujarat (India), and Thailand. We found that our model creates realistic patterns of farm locations and sizes, which are crucial for predicting disease outbreaks. When we simulated disease spread, our model showed that farms clustered together are more vulnerable to large outbreaks. This highlights the need for realistic farm data in disease prevention efforts. Our model can help public health officials in regions without detailed farm information to better plan and respond to potential disease threats. This work is a step towards better protecting both animal and human health from the spread of diseases. Read the whole study [here](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1011980).

![Figure Map](/images/Farm_distribution.png)

<span style="font-size:0.85em;">**Figure 6: average probability of large outbreak** (i.e. the proportion of simulations where the attack rate exceeds 100 farms) as a function of transmissibility for long- and short-range kernels calculated for Thailand (first row), Gujarat (second row) and Bangladesh (last row). The curves shown include our spatial model (Log Gaussian Cox Process: LGCP) trained in Thailand (yellow), Bangladesh (red) and Gujarat (blue). The markers denote simulations using empirical farm locations with original (black) and homogeneous (grey) farm sizes. The grey line represents simulations with random farm locations, providing a baseline to assess whether our spatial model (LGCP) outperforms this random distribution.</span>

Reference:
Dupas MC, Pinotti F, Joshi C, Joshi M, Thanapongtharm W, Dhingra M, Blake D, Tomley F, Gilbert M, Fournié G (2024). Spatial distribution of poultry farms using point pattern modelling: A method to address livestock environmental impacts and disease transmission risks. *PLoS Computational Biology* 20: e1011980
