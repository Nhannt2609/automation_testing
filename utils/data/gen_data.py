from faker import Faker
import time
import random
from datetime import datetime, timedelta
fake = Faker()

class GenerateJobData:
    @staticmethod
    def generate_job_data():
        clientType = random.choice(['agent', 'consignee']).upper()
        jobType = random.choice(['IMPORT', 'EXPORT', 'MISC'])
        cusRefNo = fake.bothify(text='?????')
        vessel = random.choice(['EVER GIVEN', 'EVER ULYSSES', 'UTOPIA OF THE SEAS'])
        voyage = 'V' + str(random.randint(1000, 9999))
        unloco = str(random.randint(100000, 999999))
        eta, etd = [
            (t := datetime(2025, 1, 1) + timedelta(seconds=random.randint(0, int((datetime.now() - datetime(2025, 1, 1)).total_seconds())))),
            t.strftime("%d-%m-%Y %H:%M"),
            (t + timedelta(days=1)).strftime("%d-%m-%Y %H:%M")
        ][1:]
        datetime_start = datetime.now().strftime("%d-%m-%Y %H:%M")
        datetime_end = '31-12-2025 23:59'
        agent = random.choice(['KINTRASYD', 'LAUCOMPER', 'ILUTRASYD'])
        consignee = random.choice(['KINTRASYD', 'CLAGLO', 'UCLOG'])
        return {
            "clientType": clientType,
            "jobType": jobType,
            "cusRefNo": cusRefNo,
            "vessel": vessel,
            "voyage": voyage,
            "unloco": unloco,
            "eta": eta,
            "etd": etd,
            "datetime_start": datetime_start,
            "datetime_end": datetime_end,
            "agent": agent,
            "consignee": consignee
        }    