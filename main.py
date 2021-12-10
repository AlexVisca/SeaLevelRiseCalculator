from env_variables import ENV
from appData.models import Dataset
from appCode.app import App

# from mock_data import MockDataset

def main():
    dataset = Dataset.load_from_db(ENV.CONFIG, ENV.DB)
    app = App(dataset)
    app.run()


if __name__ == '__main__':
    main()
