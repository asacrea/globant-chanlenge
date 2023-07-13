from process.factory.transform.abs_transform import AbsTransform

class DropDataframeColumns(AbsTransform):
    
    def execute(self, dfs: dict, table, parameters):
        """Changes a dataframe column names

        Args:
            df (pd.DataFrame): The dataframe to be operated on.
            map_columns (dict): A dictionary containing the column rename mappings. Eg. {"old_name": "new_name"}

        Raises:
            Exception: Raises exception when rename is not possible.

        Returns:
            [pd.DataFrame]: The Dataframe with the renamed columns
        """
        # columns = parameters["columns"]
        criterias = parameters["criterias"]
        axis = parameters["axis"]
        df = dfs[table]
        try:
            if criterias:
                for criteria in criterias:
                    df = df.loc[:,~df.columns.str.startswith(criteria)]
            if axis:
                for x in axis:
                    df.dropna(axis = x, how = 'all', inplace = True)
        except Exception as e:
            raise Exception(f"An error occurred while trying to drop the columns {e}")
        return df 
        
    def transfor_process(self, config, group_criteria):
        pass