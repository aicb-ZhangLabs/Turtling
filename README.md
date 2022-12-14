# Turtling
Code repo for paper 'Turtling: A Time-aware Neural Topic Model on NIH Grant Data'

Turtling is a time-aware neural topic model with multi-task losses which encourage diverse topics and IC classification. Turtling extracts topics from biomedical word embedding space and leverages a probabilistic time-series model which allows smooth and coherent topic evolution. We created the Grant dataset which includes 466,730 grant abstract documents and their corresponding ICs across 36 years (1985 to 2020) and tested Turtling on Grant dataset.

# Example

Run Turtling on the Grant dataset by the command below. 

```
sh grants.sh
```