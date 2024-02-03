import pandas as pd

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):

    data = data[(data['passenger_count'] > 0) & (data['trip_distance'] > 0)]

    # Crear una nueva columna lpep_pickup_date convirtiendo lpep_pickup_datetime a fecha
    data['lpep_pickup_date'] = pd.to_datetime(data['lpep_pickup_datetime']).dt.date

    # Cambiar el nombre de las columnas en Camel Case a Snake Case
    data.columns = [col.lower() for col in data.columns]

    # Renombrar columnas específicas
    data = data.rename(columns={
        'vendorid': 'vendor_id',
        'passengercount': 'passenger_count',
        'tripdistance': 'trip_distance',
        'ratecodeid': 'rate_code_id',
        'storeandfwdflag': 'store_and_fwd_flag',
        'pulocationid': 'pu_location_id',
        'dolocationid': 'do_location_id',
        'paymenttype': 'payment_type',
        'fareamount': 'fare_amount',
        'extracharges': 'extra',
        'mtatax': 'mta_tax',
        'tipamount': 'tip_amount',
        'tollsamount': 'tolls_amount',
        'improvementsurcharge': 'improvement_surcharge',
        'totalamount': 'total_amount',
        'congestionsurcharge': 'congestion_surcharge',
        'lpeppickupdatetime': 'lpep_pickup_datetime',
        'lpepdropoffdatetime': 'lpep_dropoff_datetime',
    })

    # Agregar afirmaciones
    assert data['vendor_id'].isin([1, 2]).all(), "vendor_id no es uno de los valores existentes en la columna"
    assert (data['passenger_count'] > 0).all(), "passenger_count no es mayor que 0"
    assert (data['trip_distance'] > 0).all(), "trip_distance no es mayor que 0"

    return data

@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'