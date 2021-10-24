from data_acquisition.utils import get_save_data
from data_processing.utils import get_save_train_test_data


def main():
    """Get and save the raw data.
    """
    raw_data = get_save_data()
    get_save_train_test_data(raw_data)


if __name__ == '__main__':
    main()
