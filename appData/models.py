from appData.data import Connect, SQL

# -- DATASET MODELS -- #
class Coordinate:
    def __init__(self, coords) -> None:
        self.idx: int
        self.coords: tuple = coords

        self._lat = coords[0]
        self._lon = coords[1]
        
    @property
    def coordinates(self):
        return self.coords
    
    @property
    def latitude(self):
        return self._lat
    
    @property
    def longitude(self):
        return self._lon
    
    def __repr__(self) -> str:
        return f"<{type(self)}<{self._lat}/{self._lon}>"

    def __eq__(self, other: object) -> bool:
        if self._lat == other._lat and self._lon == other._lon:
            return True
        else:
            return False

    def __gt__(self, other: object) -> bool:
        if self._lat > other._lat or self._lon > other._lon:
            return True
        else:
            return False

    def __lt__(self, other: object) -> bool:
        if self._lat < other._lat or self._lon < other._lon:
            return True
        else:
            return False
    

class Dataset:
    def __init__(self, coord_list) -> None:
        self._coordinates = coord_list
    
    def __repr__(self) -> str:
        return f"{type(self._coordinates)}len={len(self._coordinates)}\n"

    def __len__(self):
        return len(self._coordinates)
    
    def get_data(self):
        data = list()
        for point in self._coordinates:
            data.append(point.coordinates)
        
        return data

    @property
    def coordinates(self):
        return self._coordinates

    @classmethod
    def load_from_db(cls, config, database):
        datasets = list()
        with Connect(config, database) as db:
            crs = db.cursor()
            table_list = SQL.inject(crs, "SHOW tables;")
            for table in table_list:
                query = f"SELECT * FROM {table[0]};"
                result = SQL.inject(crs, query)
                coord_list = list()
                for coord in result:
                    point = Coordinate(coord)
                    coord_list.append(point)
                # --
                datasets.append(
                    Dataset(coord_list))
            
        return datasets

