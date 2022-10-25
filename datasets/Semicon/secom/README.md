# SECOM Dataset

## Usage
```python
import pandas as pd

data = pd.read_pickle('proc/data.pkl')

df_header = data['meta']         # meta information
df_value = data['measurements']  # sensor measurements

assert df_header.shape[0] == df_value.shape[0]
```

### Notes
* Rows of `df_header` and `df_value` are paired.

## Scripts
|  Name         | Description                   |
|  ---          |  ---                          |
| ``trans.ipynb`` | Processing raw (raw -> proc)  |
| `eda.ipynb`   | Quick EDA                     |


## Source
http://archive.ics.uci.edu/ml/datasets/secom

