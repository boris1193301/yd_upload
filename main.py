import yadisk
from config import YD_API_TOKEN, SOURCE_PATH, TARGET_PATH

if __name__ == "__main__":
    y = yadisk.YaDisk(token=YD_API_TOKEN)
    y.upload(SOURCE_PATH, TARGET_PATH, overwrite=True)
