import datetime
from etl_factory.factory.abs_factory import AbsFactory
from etl_factory.factory.loader import load_class
from etl_factory.factory.transform.abs_transform import AbsTransform
from etl_factory.factory.extract.abs_extraction import AbsExtraction
from etl_factory.factory.load.abs_load import AbsLoad

class ETL_Factory(AbsFactory):
    '''
        This class allow you to create a ETL object based in Factory Design pattern
    '''
    def __init__(self, parameters) -> None:
        super().__init__()
        self.config = parameters['itemList']
        self.bucket_name = parameters['bucket_name']
        self.key_name = parameters['key_name']
        self.load_path = parameters['load_path']
        self.source_file_name = parameters['source_file_name']
        self.data = None
        self.transformed_data = None
        self.file_name = None

    def extract_method(self):

        print("--------------------------------------")
        print("Extracting Files:\n")
        method = [x for x in self.config['extract']][0]
        path = self.config['extract'][method]['path']
        parameters = self.config['extract'][method]['parameters']
        module = load_class(path, \
                            method, \
                            AbsExtraction)
        response, self.data = module.extract(parameters)
        
        print(f"{response['Validation']}: {response['Reason']}")
        print(f"Location: {response['Location']}")

    def transform_method(self):

        print("-------------------------------------")
        print("Transforming Files:\n")

        for method in self.config['transform']:
            path = self.config['transform'][method]['path']
            module = load_class(path, \
                                method, \
                                AbsTransform)
            result, self.transformed_data = module.execute(
                dfs = self.data,
                parameters = self.config["transform"][method]['parameters']
            )
            print(self.transformed_data)

    def load_method(self):
        
        print("--------------------------------------")
        print(f"Loading Files to: {self.load_path}\n")

        fecha_actual = datetime.datetime.now()
        year = fecha_actual.year
        month = fecha_actual.month
        day = fecha_actual.day

        self.load_path = f"{self.load_path}/{year}/{month}/{day}"

        factory_load = load_class("CSVLoad", \
                                  "process.factory.load", \
                                  AbsLoad)
        factory_load.execute(self.transformed_data, \
                             self.load_path, \
                             self.key_name)
