import torch
from datasets import load_from_huggingface
from fastai.vision.all import *

class CustomImageDataset(torch.utils.data.Dataset):
    def __init__(self, images, labels):
        self.images = images
        self.labels = labels

    def __len__(self):
        return len(self.labels)

    def __getitem__(self, idx):
        image = self.images[idx]
        label = self.labels[idx]
        return np.array(image.resize((224,224), resample=0)), label


def get_dataset_huggingface():
    ds = load_from_huggingface()
    ds = ds.class_encode_column("L3")
    #num_classes = ds.features["L3"].num_classes
    ds = ds.train_test_split(test_size=0.2, seed=42)
    train_data = CustomImageDataset(ds["train"]["image"], ds["train"]["L3"])
    test_data = CustomImageDataset(ds["test"]["image"], ds["test"]["L3"])
    train_dataloader = DataLoader(train_data, batch_size=32)
    test_dataloader = DataLoader(test_data, batch_size=32)
    dls = DataLoaders(train_dataloader, test_dataloader)

    train_features, train_labels = next(iter(train_dataloader))
    print(f"Feature batch shape: {train_features.size()}")
    print(f"Labels batch shape: {train_labels.size()}")
    img = train_features[0].squeeze()
    label = train_labels[0]
    plt.imshow(img)
    plt.savefig("test.png")
    print(f"Label: {label}")

    learn = vision_learner(
            dls,
            resnet34,
            metrics=[error_rate, accuracy],
            concat_pool=True,
            splitter=default_split,
        ).to_fp16()
    return dls, [error_rate, accuracy]
get_dataset_huggingface()