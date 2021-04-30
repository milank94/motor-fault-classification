from data_acquisition.main import get_data,Dataset

import config


def local_run() -> Dataset:
    """
    This method runs a train pipleine locally and returns
    trained model object.
    """

    # load data
    dataset = get_data()
    return dataset


if __name__ == "__main__":
    if config.COMPUTE == 'local':
        dataset = local_run()
