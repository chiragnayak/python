import argparse
import csv
import smtplib
import sys
import traceback
from datetime import datetime, timedelta
import json
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import requests

DISTRICT_MAPPING = {
    "PUNE": "363",
    # "THANE": "392",
    # "MUMBAI": "395"
}

SUBSCRIBER_FILENAME = "subscription"

DAYS = 14


def send_email(subject=None, message_to_send=None, emails_to_sent=None):
    MESSAGE = MIMEMultipart('alternative')
    MESSAGE['subject'] = subject
    MESSAGE['From'] = "no_reply_vac@vmware.com"

    smtp_server = "smtp.vmware.com"
    port = 25  # For starttls
    sender_email = "no_reply_vac@vmware.com"
    server = None
    # Try to log in to server and send email
    try:
        server = smtplib.SMTP(smtp_server, port)
        if emails_to_sent is None or len(emails_to_sent) == 0:
            print("NO EMAILS TO SEND")
            return
        for receiver in emails_to_sent:
            receiver = receiver.strip()
            MESSAGE['To'] = receiver
            print("SENDING EMAIL TO : ", receiver)
            email_body = MIMEText(message_to_send, 'html')
            MESSAGE.attach(email_body)
            server.sendmail(sender_email, receiver, MESSAGE.as_string())
        print("EMAIL SENT..")
    except Exception as e:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        traceback.print_exception(exc_type, exc_value, exc_traceback, file=sys.stdout)
        print("EXCEPTION OCCURRED WHILE EMAIL PROCESSING!!")
        print(e)
    finally:
        server.quit()


def parse_arguments():
    parser = argparse.ArgumentParser(description='RECEIVES LIST OF CITIES TO POLL')
    parser.add_argument('--cities', default='PUNE', help="CITIES TO POLL")
    parser.add_argument('--age', default='18', help="CITIES TO POLL")
    parser.add_argument('--dose', default='1', help="DIOSAGE")
    args = parser.parse_args()
    return args


if __name__ == "__main__":

    # get cities
    args = parse_arguments()
    CITIES = list(args.cities.split(","))
    AGE = int(args.age)
    DOSE = int(args.dose)

    # get subscribers
    subscribers = dict()
    try:
        SUBSCRIBER_FILENAME = SUBSCRIBER_FILENAME + "_{}.csv".format(AGE)
        with open(SUBSCRIBER_FILENAME, 'r') as csvFile:
            cities = csv.DictReader(csvFile)
            for city in cities:
                city_name = city['CITY']
                subs_list = list(city['EMAILS'].split(","))
                subscribers[city_name] = subs_list
    except Exception as e:
        print("Error Occurred - {} : {}".format(e.__class__.__name__, e))
        print(traceback.format_exc())

    finally:
        csvFile.close()

    NO_SLOT_AT_ALL = True
    temp_date = datetime.today() + timedelta(days=0)
    TODAYS_DATE = temp_date.strftime('%d-%m-%Y')

    DATES = list()
    for day in range(0, DAYS):
        X_DATE = datetime.today() + timedelta(days=day)
        REQUIRED_DATE = X_DATE.strftime('%d-%m-%Y')
        DATES.append(REQUIRED_DATE)

    for date in DATES:
        for city_str in CITIES:
            city_str = city_str.strip()
            city = DISTRICT_MAPPING[city_str]

            city_message = list()
            display = "FOR DISTRICT : {} | {}".format(city_str, date)
            city_message.append("<br><br>")
            city_message.append("=" * 40)
            city_message.append(display)
            city_message.append("=" * 40)
            print(display)
            headers = {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
            request_text = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id={}&date={}".format(
                city, date)
            resp = requests.get(request_text, headers=headers)

            if resp.status_code != 200:
                # This means something went wrong.
                raise Exception("API FAILED -> CODE = {}".format(resp.status_code))

            response = json.loads(resp.text)
            available = False

            if len(response["sessions"]) == 0:
                message_no_session = "NO CENTRE AVAILABLE"
                print(message_no_session)
                city_message.append("x" * 40)
                city_message.append(message_no_session)
                city_message.append("x" * 40)
                continue
            else:
                for session in response["sessions"]:
                    age_limit = str(session["min_age_limit"])
                    slots_available = session["available_capacity"]
                    slot_available_dose_1 = session["available_capacity_dose1"]
                    slot_available_dose_2 = session["available_capacity_dose2"]

                    if DOSE == 1:
                        required_dose_slot = slot_available_dose_1
                    else:
                        required_dose_slot = slot_available_dose_2

                    if session["date"] in DATES and age_limit == str(AGE) \
                            and slots_available > 1\
                            and required_dose_slot > 1:
                        session_text = list()
                        session_text.append("===" * 10)
                        session_text.append("SLOT AVAILABLE")
                        session_text.append("===" * 10)
                        session_text.append(str(session["name"]))
                        session_text.append("CENTER NAME : {} ".format(str(session["name"])))
                        session_text.append("ADDRESS : {} ".format(str(session["address"])))
                        session_text.append("PINCODE : {} ".format(str(session["pincode"])))
                        session_text.append("DATE : {} ".format(str(session["date"])))
                        session_text.append("AVAILABLE CAPACITY : {} ".format(str(session["available_capacity"])))
                        session_text.append("AVAILABLE DOSE {} CAPACITY : {} ".format(DOSE, str(required_dose_slot)))
                        session_text.append("FEE TYPE : {} ".format(str(session["fee_type"])))
                        session_text.append("TIME SLOTS : {} ".format(str(session["slots"])))

                        # maps link
                        google_maps = "https://www.google.com/maps/place/" + str(session["address"])
                        cowin_websige = "https://www.cowin.gov.in/home"
                        session_text.append("<a href=\"{}\">LOCATION ON MAP</a>".format(google_maps))
                        session_text.append("<a href=\"{}\">COWIN website</a>".format(cowin_websige))
                        session_text.append("<br>" * 1)

                        available = True
                        NO_SLOT_AT_CENTER = False
                        NO_SLOT_AT_ALL = False
                        x = "<br>".join(session_text)
                        city_message.append(x)

                        message = "+++ SLOT AVAILABLE FOR {} Yr AT {} | PIN {} | {} +++".format(AGE,
                                                                                                str(session["name"]),
                                                                                                str(session["pincode"]),
                                                                                                date)
                        print(message)
                    else:
                        message = "xxx NO SLOT REMAINING FOR {} Yr AT {} | PIN {} | {} xxx".format(AGE,
                                                                                                   str(session["name"]),
                                                                                                   str(session[
                                                                                                           "pincode"]),
                                                                                                   date)
                        print(message)
                        # city_message.append(message)

            if available:
                x = "<br>".join(city_message)
                RECEIVERS = subscribers[city_str]
                send_email(subject="AVAILABLE | AGE: {} | CITY : {}, BOOK NOW".format(AGE, city_str), message_to_send=x,
                           emails_to_sent=RECEIVERS)
                available = False

    # if NO_SLOT_AT_ALL:
    #     send_email("Subject: CITY | {} | AGE {} | NO VACCINE SLOTS AVAILABLE"
    #                "\n"
    #                "\n"
    #                "{}"
    #                "\n"
    #                "\n"
    #                "{}".format(TODAYS_DATE, AGE, CITIES, DATES), receiver_emails)
