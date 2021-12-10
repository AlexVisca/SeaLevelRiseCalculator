import random as rndm

from appData.models import Coordinate, Dataset

class MockDataset:
    def __init__(self, dataset_list, copies) -> list:
        self._dataset_list = dataset_list
        self.mock_dataset = list()

        for dataset in self._dataset_list:
            self.mock_dataset.append(dataset)
        
        self.copy(copies)
    
    def __len__(self):
        return len(self.mock_dataset)
    

    @property
    def as_list(self):
        return self.mock_dataset

    def _load_mock_dataset(self, dataset: object):
        coord_list = list()
        for point in dataset.coordinates:
            sign = rndm.choice('+-')
            float_0_1 = rndm.random()
            coord_tuple = point.coords
            if sign == '+':
                coord_list.append(Coordinate(
                    (coord_tuple[0] + float_0_1, coord_tuple[1] + float_0_1)))
            if sign == '-':
                coord_list.append(Coordinate(
                    (coord_tuple[0] - float_0_1, coord_tuple[1] - float_0_1)))
            
            false_dataset = Dataset(coord_list)
        
        return false_dataset

    def copy(self, copies=None):
        if not copies:
            copies=6

        dset_to_copy = self._dataset_list[1]
        
        for i in range(copies):
            false_dataset = self._load_mock_dataset(dset_to_copy)
            self.mock_dataset.append(false_dataset)
        
        return self.mock_dataset
        
