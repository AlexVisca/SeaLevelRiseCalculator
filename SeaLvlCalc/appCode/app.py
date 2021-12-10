from appCode.controllers import Controller
from appCode.views import View

import time


class App:
    def __init__(self, datasets) -> None:
        self.dataset = datasets
        self.calculate = Controller(self.dataset)
        self.view = View(self.dataset)
    
    def run(self):
        # -- Test Data Integrity
        self.view.display(f"Testing data integrity...")
        running, err = self.calculate.check()
        if not running:
            self.view.display("Test of data integrity: Failed")
            self.view.display(err)
            exit()
        self.view.display("Test of data integrity: Passed")
        # --
        self.view.display(f"Starting calculations...")
        start_time = time.perf_counter()
        # -- View ALL Datasets (WARNING: May contain ALOT of data!)
        # data = self.calculate._data()
        # self.view.display_data(data)
        # --
        print("...")
        # -- Calculate Mean
        self.view.display(F"Calculating mean across {len(self.dataset)} datasets")
        # self.view.display_prompt()
        tables_list = self.calculate.variance_tables()
        results = self.calculate.mean(tables_list)
        # self.view.display_results(results)
        # --
        print("...")
        # -- Calculate Standard Deviation
        self.view.display(F"Calculating standard deviation across {len(self.dataset)} datasets with {self.dataset[0].__len__()} coordinates")
        print("...")
        print("Calculations complete")
        self.view.display_prompt()
        print("Results:")
        analysis = self.calculate.standard_deviation(results)
        self.view.display_analysis(analysis)
        # --
        end_time = time.perf_counter()
        total = end_time - start_time
        total_time = f"Data calculated in {total:.3f} secs"
        self.view.display(total_time)
