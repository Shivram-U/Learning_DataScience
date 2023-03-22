import numpy as np
from scipy import stats as stt
import statistics as st
heights = np.array([1,2,3,4,5,5,6,1,2,2,3,4,4])

print("Mean : ",np.mean(heights))
print("Median : ",np.median(heights))
print("Variance : ",np.var(heights))
print("Variance : ",round(np.var(heights),2))
print("Variance : ",round(np.std(heights),2))
print("Mode: ",stt.mode(heights))

print(st.quantiles(heights,n=1))
print(st.quantiles(heights,n=2))
print(st.quantiles(heights,n=3))
print(st.quantiles(heights,n=4))

h = np.array([14, 19, 20, 22, 24, 26, 27, 30, 30, 31, 36, 38, 44, 47])
q3 = (np.percentile(h,75))
q1 = (np.percentile(h,25))
print(q3-q1)

r = max(h)-min(h)
print(r)