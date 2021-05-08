from datetime import datetime, timedelta
import json
import smtplib
import requests


CITIES = ["363"]
DAYS = [0, 1, 2, 3, 4, 5, 6, 7]
AGE = 18


def send_email(message_to_send=None):
    smtp_server = "smtp.vmware.com"
    port = 25  # For starttls
    sender_email = "no_reply_pycowin@vmware.com"
    receiver_email = "cnayak@vmware.com"

    # Try to log in to server and send email
    try:
        server = smtplib.SMTP(smtp_server,port)
        server.sendmail(sender_email, receiver_email, message_to_send)
    except Exception as e:
        print("EXCEPTION OCCURED!!")
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

    for city in CITIES:
        city_message = list()
        display = "FOR CITY : {} ".format(city)
        NO_SLOT_CITY = True
        city_message.append("\n\n")
        city_message.append("=" * 40)
        city_message.append(display)
        city_message.append("=" * 40)
        print(display)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        request_text = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id={}&date={}".format(city, TODAYS_DATE)
        resp = requests.get(request_text, headers=headers)

        if resp.status_code != 200:
            # This means something went wrong.
            raise Exception("API FAILED -> CODE = {}".format(resp.status_code))


        response = json.loads(resp.text)
        available = False

        if len(response["sessions"]) == 0:
            city_message.append("x" * 40)
            city_message.append("NO CENTRE AVAILABLE FOR PINCODE {}".format(city))
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
                    session_text.append("CENTER NAME : {}".format(str(session["name"])))
                    session_text.append("ADDRESS : {}".format(str(session["address"])))
                    session_text.append("PINCODE : {}".format(str(session["pincode"])))
                    session_text.append("AVAILABLE : {}".format(str(session["available_capacity"])))
                    session_text.append(str(session["vaccine"]))
                    session_text.append(str(session["slots"]))
                    session_text.append("\n" * 1)
                    available = True
                    NO_SLOT_CITY = False
                    NO_SLOT_AT_ALL = False
                    x = "\n".join(session_text)
                    city_message.append(x)

                if NO_SLOT_CITY:
                    city_message.append("xxx NO SLOT AVAILABLE FOR THIS DATE xxx\n\n")

        if available:
            city_message.insert(0, "Subject: AGE: {} | PIN : {} COVID VACCINE AVAILABLE, BOOK NOW".format(AGE, city))
            x = "\n".join(city_message)
            send_email(x)
            available = False

    if NO_SLOT_AT_ALL:
        send_email("Subject: {} NO VACCINE SLOTS AVAILABLE"
                   "\n"
                   "\n"
                   "{}".format(TODAYS_DATE, CITIES))






