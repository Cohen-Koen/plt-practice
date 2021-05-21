import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

sal = 79800
#cost of housing
housing = 35700
#insurance
insurance = (500 + 1592 + 4364)
car = 3500
#utilities
#utilities = "included in housing"

#                                     save half of what isnt used
# entertainment is the other half of unused
clothing = 150

savings = 24672

misc = 24672



cmap = plt.get_cmap("gnuplot2")
colors = [cmap(i) for i in [.1,0.25 ,.4,0.6, .10]]

values = [sal,housing,savings,misc,insurance,car,clothing,]
labels = ["Salary", "Housing","Savings", "Misc", "Insurance", "Car", "Clothing \n $150"]
plt.bar(labels,values,color = colors)
plt.savefig("graph.png", dpi=400)
plt.show()

