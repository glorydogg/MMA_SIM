<<<<<<< HEAD
from aws.aws_uploader import S3Uploader
=======
from util.awsuploader import S3Uploader
>>>>>>> 548563b36728eb347a54def1cad928a8cc4c40d8
import pandas as pd 
import os

uploader = S3Uploader()

class FightLogger:
    def __init__(self, filename= "fight_history.csv"):
        self.filename = filename
        
    def log_fight(self, fight_data: dict):
        """ Save locally """
        df = pd.DataFrame([fight_data])
        df.to_csv(self.filename,
                  mode="a",
                  index=False,
                  header= not os.path.exists(self.filename))
        print(f"\n[Log] Fight recorded to {self.filename}")

<<<<<<< HEAD

        # Upload to s3
        success = uploader.upload(self.filename, self.filename)

        if success:
            print(f"[Upload] Uploaded to {self.filename} to s3!")
        else:
            print(f"[Upload] to s3 failed!")


=======
>>>>>>> 548563b36728eb347a54def1cad928a8cc4c40d8
    def load_history(self):
        """ Load full fight history into dataframe """
        if not os.path.exists(self.filename):
            return pd.DataFrame()
        return pd.read_csv(self.filename)

