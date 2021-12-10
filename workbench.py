from env_variables import ENV
from appData.models import Dataset
from appCode.app import App

from mock_data import MockDataset

def main():
    print(f"Sea-Level Rise Calculator")
    dataset = MockDataset(Dataset.load_from_db(ENV.CONFIG, ENV.DB), copies=28).as_list
    print(f"Generating mock datasets...")
    app = App(dataset)
    app.run()


if __name__ == '__main__':
    main()
