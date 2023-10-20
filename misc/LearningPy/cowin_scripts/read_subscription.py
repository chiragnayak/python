import csv
import traceback

from misc.LearningPy import send_email

FILENAME = "subscription.csv"

if __name__ == "__main__":
    try:
        with open(FILENAME, 'r') as csvFile:
            cities = csv.DictReader(csvFile)
            for city in cities:
                city_name = city['CITY']
                subscribers = list(city['EMAILS'].split(","))
                send_email("Test Email", "This is test email, testing the new approach", subscribers)
    except Exception as e:
        print("Error Occurred - {} : {}".format(e.__class__.__name__, e))
        print(traceback.format_exc())

    finally:
        csvFile.close()