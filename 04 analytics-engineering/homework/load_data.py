import io
import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
    df_list = []

    taxi_dtypes = {
        'dispatching_base_num': str,
        'PUlocationID': pd.Int64Dtype(),
        'DOlocationID': pd.Int64Dtype(),
        'SR_Flag': str,
        'Affiliated_base_number': str
    }

    base_url = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/fhv/'

    for month in range(1, 13):
        url = f'{base_url}fhv_tripdata_2019-{month:02d}.csv.gz'
        df = pd.read_csv(url, sep=',', compression='gzip', dtype=taxi_dtypes)
        df_list.append(df)

    df_combined = pd.concat(df_list, ignore_index=True)
    return df_combined

@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'