import math


class Controller:
    def __init__(self, dataset_) -> None:
        self._dataset = dataset_
    
    def __str__(self):
        return [f"{type(d_set)} {d_set}" for d_set in self._dataset]
    

    def _data(self) -> list[list[tuple]]:
        data = list()
        coord_list = [dset_obj.coordinates for dset_obj in self._dataset]
        for list_of_coords in coord_list:
            data.append([coord_obj.coordinates for coord_obj in list_of_coords])
        
        return data
    

    def check(self) -> str:
        try:
            bool_list = list()
            for dset in self._dataset:
                set_len = dset.__len__()
                if set_len <= 0:
                    bool_list.append(False)
                if set_len > 0:
                    bool_list.append(True)
                    
            return all(bool_list), NotImplemented

        except Exception as exc:
            return False, exc


    def variance_tables(self):
        table_list = list()
        _dataset_list = self._data()
        i = 0
        try:
            for _dataset in _dataset_list:
                first = _dataset_list[i]
                secnd = _dataset_list[i +1]
                compare = self._variance(first, secnd)

                table_list.append(compare)
                i += 1

        except IndexError:
            pass

        return table_list


    def _variance(self, first, secnd):
        comparison = list()
        for idx, coordinate in enumerate(first):
            coord = secnd[idx]
            compare = (coordinate[0] - coord[0],
                        coordinate[1] - coord[1])
            comparison.append(compare)

        return comparison

    
    def mean(self, table_list):
        count = len(table_list)
        mean_list = list()
        for row in range(len(table_list[0])):
            lat_sum = float()
            lon_sum = float()
            i = 0
            for table in table_list:
                lat_sum += table[i][0]
                lon_sum += table[i][1]
            i +=1

            lat_var_avg = lat_sum / count
            lon_var_avg = lon_sum / count

            mean_list.append((lat_var_avg, lon_var_avg))

        return mean_list

    def standard_deviation(self, mean_list):
        count = len(mean_list) # 383
        lat_sum = float()
        lon_sum = float()
        for row in mean_list:
            lat_sum += row[0]
            lon_sum += row[1]
        
        lat_std_dev = math.sqrt((lat_sum**2) / count)
        lon_std_dev = math.sqrt((lon_sum**2) / count)

        return (lat_std_dev, lon_std_dev)


# -- Code Snippets

    def variance(self):
        latitudes = []
        longitudes = []
        for _dataset in self._dataset:
            _lat = []
            _lon = []
            for point in _dataset.coordinates:
                _lat.append(point.latitude)
                _lon.append(point.longitude)
            latitudes.append(_lat)
            longitudes.append(_lon)

        variance = list()
        for i in range(len(_dataset.coordinates)):
            variance.append(
                (latitudes[0][i-1] - latitudes[1][i-1], 
                longitudes[0][i-1] - longitudes[1][i-1]))

        return variance
        


    def raw_data(self):
        data = list()
        for dset_obj in self._dataset:
            coord_list = dset_obj.coordinates
            _data = list()
            for coord_obj in coord_list:
                point = coord_obj.coordinates
                _data.append(point)
            data.append(_data)
        
        return data
        


