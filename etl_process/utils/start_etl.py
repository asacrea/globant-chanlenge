import json
import os
from etl_factory.factory.factory_etl import ETL_Factory

def lambda_handler(event, context):

    parameters = event['parameters']

    try:

        etl = ETL_Factory(parameters)
        etl.extract_method()
        etl.transform_method()
        etl.load_method()

        return {'Validation': 'SUCCESS'}

    except Exception as e:

        print(f'An error occurred: {str(e)}')
        return {'Validation': 'FAILURE'}
