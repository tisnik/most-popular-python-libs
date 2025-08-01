from datasets import load_dataset

dataset_id = "polygraf-ai/human-sentences-1M-sample-v2"

dataset = load_dataset(dataset_id)

print(dataset)
