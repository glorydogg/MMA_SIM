from util.awsuploader import S3Uploader
import pandas as pd 
import os

class FightLogger:
    def __init__(self, filename= "fight_history.csv"):
        self.filename = filename
        
    def log_fight(self, fight_data: dict):
        """ Append fight data to csv """
        df = pd.DataFrame([fight_data])
        df.to_csv(self.filename,
                  mode="a",
                  index=False,
                  header= not os.path.exists(self.filename))
        print(f"\n[Log] Fight recorded to {self.filename}")

    def load_history(self):
        """ Load full fight history into dataframe """
        if not os.path.exists(self.filename):
            return pd.DataFrame()
        return pd.read_csv(self.filename)

