import pandas as pd
import os
class read_file():
    def __init__(self,filename="words_to_learn"):
        self.to_learn={}
        try:
            current_dir = os.path.dirname(os.path.abspath(__file__))
            self.filename = os.path.join(current_dir, "data", "words_to_learn.csv")
            self.df = pd.read_csv(self.filename)
        except FileNotFoundError:
            current_dir = os.path.dirname(os.path.abspath(__file__))
            self.filename = os.path.join(current_dir, "data", filename)
            self.df = pd.read_csv(self.filename)
            self.to_learn = self.df.to_dict(orient="records")
        else:
            self.to_learn = self.df.to_dict(orient="records")
    def condition(self):
        cols=self.df.columns
        condition = (
            ~self.df[cols[0]].apply(lambda x: isinstance(x, (float, int)) or len(str(x)) < 2)
            & ~self.df[cols[1]].apply(lambda x: isinstance(x, (float, int)) or len(str(x)) < 2)
        )        
        self.df = self.df[condition]
    def data_to_csv(self, data):
        data_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
        if not os.path.exists(data_directory):
            os.makedirs(data_directory)
        
        if len(data) > 0:
            data.to_csv(os.path.join(data_directory, "words_to_learn.csv"), index=False)

    def get_data(self):
        return self.df