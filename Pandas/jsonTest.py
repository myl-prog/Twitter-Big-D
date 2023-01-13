from random import randint
import smtplib
import os
import ssl 
from time import sleep
import pandas as pd



if __name__ == '__main__':

	df = pd.read_json('Test.json',encoding = "latin")
	Tweeter_list=df.values.tolist()
	print(df);

