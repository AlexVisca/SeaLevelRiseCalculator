import pandas as pd

class View:
    def __init__(self, dataset_) -> None:
        self._dataset = dataset_
        self.prompt = '='*24
    
    def display(self, stdout):
        print(stdout)

    def display_prompt(self):
        print(self.prompt)

    def display_data(self, data):
        for idx, coord_list in enumerate(data):
            df = pd.DataFrame(data=coord_list, columns=['Latitude', 'Longitude'])
            print(f"DATASET {idx+1}: `coordinates`")
            print(df)
    
    def display_results(self, data):
        var = pd.DataFrame(data=data, columns=['delta(lat)', 'delta(lon)'])
        print("TABLE `average`")
        print(var)

    def display_analysis(self, std_dev):
        cardinal = 'East'
        std = std_dev[0] + std_dev[1]
        std_avg = std / 2
        m_convert = std_avg * 10
        string = f"Shoreline erosion calculated at {m_convert:2f} metres {cardinal} over a {len(self._dataset)} year period"
        print(string)

    def tree(self, data):
        print(f"|-{type(data)}{len(data)}")
        for item in data:
            print(f"|--{type(item)}  {len(item):<8}", )
            for coord in item:
                print(f"|----{type(coord)} {len(coord):<8}", )
                break