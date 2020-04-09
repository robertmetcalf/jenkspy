#!/usr/bin/env python

# system packages
import csv

# third-party packages
import jenkspy
import pandas as pd


def test ():
	# read the CSV file
	df = pd.read_csv('jenkspy-test.csv', dtype={'value': int}, usecols=['value'])

	# create jenks natural breaks (bin_count = 6 works, 7 breaks)
	bin_count = 7
	bins = jenkspy.jenks_breaks(df['value'], nb_class=bin_count)
	print(f'--> BINS {bins}')
	print(f'--> COUNT {len(bins)}')

	# set the rank for each value
	rank_labels = range(1, bin_count + 1)
	#pd_cut = pd.cut(df['value'], bins=bins, duplicates='drop', labels=rank_labels, include_lowest=True)
	pd_cut = pd.cut(df['value'], bins=bins, labels=rank_labels, include_lowest=True)
	df['rank'] = pd_cut

	df.to_csv('jenkspy-test-results.csv', index=False)


if __name__ == '__main__':
	test()
