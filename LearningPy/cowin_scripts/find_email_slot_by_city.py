import traceback
from datetime import datetime, timedelta
import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import requests
import sys, webbrowser

CITIES = ["363"]

DISTRICT_MAPPING = {
    "363":"PUNE",
    "392":"THANE",
    "108":"CHANDIGARH"
}

DAYS = [0, 1, 2, 3, 4, 5, 6, 7]
AGE = 18
RECEIVERS = ["cnayak@vmware.com", "gtarun@vmware.com", "diyewarr@vmware.com"]


def send_email(subject=None, message_to_send=None, emails_to_sent=None):

    MESSAGE = MIMEMultipart('alternative')
    MESSAGE['subject'] = subject
    MESSAGE['From'] = "no_reply_vac@vmware.com"

    smtp_server = "smtp.vmware.com"
    port = 25  # For starttls
    sender_email = "no_reply_vac@vmware.com"

    # Try to log in to server and send email
    try:
        server = smtplib.SMTP(smtp_server,port)
        for receiver in emails_to_sent:
            MESSAGE['To'] = receiver
            print("SENDING EMAIL TO : ", receiver)
            email_body = MIMEText(message_to_send ,'html')
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


if __name__ == "__main__":
    NO_SLOT_AT_ALL = True
    temp_date = datetime.today() + timedelta(days=0)
    TODAYS_DATE = temp_date.strftime('%d-%m-%Y')

    DATES = list()
    for day in DAYS:
        X_DATE = datetime.today() + timedelta(days=day)
        REQUIRED_DATE = X_DATE.strftime('%d-%m-%Y')
        DATES.append(REQUIRED_DATE)

    for date in DATES:
        for city in CITIES:
            city_message = list()
            display = "FOR DISTRICT : {} | {}".format(DISTRICT_MAPPING[city], date)
            city_message.append("<br><br>")
            city_message.append("=" * 40)
            city_message.append(display)
            city_message.append("=" * 40)
            print(display)
            headers = {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
            request_text = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id={}&date={}".format(city, date)
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
                    if session["date"] in DATES and age_limit == str(AGE) and slots_available > 1:
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
                        session_text.append("VACCINE TYPE : {} ".format(str(session["vaccine"])))
                        session_text.append("SLOTS : {} ".format(str(session["slots"])))

                        #maps link
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
                    else:
                        message = "xxx NO SLOT AVAILABLE FOR {} Yr AT {} | PIN {} | {} xxx".format(AGE, str(session["name"]), str(session["pincode"]), date)
                        print(message)
                        # city_message.append(message)

            if available:
                x = "<br>".join(city_message)
                send_email("AVAILABLE | AGE: {} | CITY : {}, BOOK NOW".format(AGE, DISTRICT_MAPPING[city]), x, RECEIVERS)
                available = False

    # if NO_SLOT_AT_ALL:
    #     send_email("Subject: CITY | {} | AGE {} | NO VACCINE SLOTS AVAILABLE"
    #                "\n"
    #                "\n"
    #                "{}"
    #                "\n"
    #                "\n"
    #                "{}".format(TODAYS_DATE, AGE, CITIES, DATES), receiver_emails)






