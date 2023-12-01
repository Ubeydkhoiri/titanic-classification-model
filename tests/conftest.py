import pytest

from classification_model.config.core import config
from classification_model.processing.data_manager import load_dataset


@pytest.fixture()
def sample_input_data():
    data = load_dataset(file_name=config.app_config.test_data_file)
    input_data = data[:100]
    return input_data
