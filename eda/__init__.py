
# coding: utf-8


from eda.describe import describe

class ProfileReport(object):

    def __init__(self, df, **kwargs):
        
        sample = kwargs.get('sample', df.head())

        description_set = describe(df, **kwargs)

        self.description_set = description_set

    def get_description(self):
        
        return self.description_set

    def get_rejected_variables(self, threshold=0.9):
        
        variable_profile = self.description_set['variables']
        result = []
        if hasattr(variable_profile, 'correlation'):
            result = variable_profile.index[variable_profile.correlation > threshold].tolist()
        return  result