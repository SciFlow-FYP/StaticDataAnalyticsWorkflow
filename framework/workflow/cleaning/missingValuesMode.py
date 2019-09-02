import pandas as pd
import numpy as np
import statistics
from dataType import *
from userScript import *

df = pd.read_csv(outputDataset)
#********************************** WHAT HAPPENS WHEN MODE IS NAN *************************************************************************
colNames = modeColumns

for col in colNames:
	modeOfCol = statistics.mode(df[col])
	df[col].fillna(modeOfCol, inplace = True)


df.to_csv (outputDataset, index = False, header=True)
