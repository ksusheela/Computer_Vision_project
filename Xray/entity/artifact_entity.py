from dataclasses import dataclass
#import torch
from torch.utils.data.dataloader import DataLoader


@dataclass
class DataIngestionArtifact:
    train_file_path: str

    test_file_path: str