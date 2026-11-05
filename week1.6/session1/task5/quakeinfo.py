# Week 1.6, Session 1: Task 5

# Write a program here that uses the QuakeFeed and QuakeDataset
# classes to download earthquake data from a USGS data feed,
# analyze it and display the results

# See README.md for full details of what is required and what
# program output should look like

from dataset import QuakeDataset
from feed import QuakeFeed
from quake import Quake

sig = input("Please enter a significance level ")
time = input("Please enter a time period ")

qf = QuakeFeed(sig,time)

dataset = QuakeDataset(qf)

dataset.read_feed()

print(dataset)
print(f"Mean depth: {dataset.mean_depth()}")
print(f"Mean magnitude: {dataset.mean_magnitude()}")

print(f"Strongest quake occurred at {dataset.strongest_quake().when}")
