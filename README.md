# jenkspy

Jenkspy test when the results contain multiple zero entries

## Description

I have a data set that I break into 7 bins. The results include the zero value, twice. Here is an example.

```python
bin_count = 7
bins = jenkspy.jenks_breaks(df['value'], nb_class=bin_count)
print(f'BINS {bins}')

BINS [0.0, 0.0, 10435.0, 11643.0, 12476.0, 13337.0, 16116.0, 27125.0]
```

If the data is broken into 6 bins it works. Here is the output.

```python
BINS [0.0, 10191.0, 11529.0, 12405.0, 13286.0, 16073.0, 27125.0]
```

See the `jenkspy-test.py` file for the test. The data is in `jenkspy-test.csv`
