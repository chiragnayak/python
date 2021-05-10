from datetime import datetime, timedelta
import json
import smtplib
import requests
import sys, webbrowser

CITIES = ["363"]
DAYS = [0, 1, 2, 3, 4, 5, 6, 7]
AGE = 18
receiver_emails = ["cnayak@vmware.com", "gtarun@vmware.com","diyewarr@vmware.com"]


def send_email(message_to_send=None, receiver_emails=None):
    smtp_server = "smtp.vmware.com"
    port = 25  # For starttls
    sender_email = "no_reply@vmware.com"

    # Try to log in to server and send email
    try:
        server = smtplib.SMTP(smtp_server,port)
        for receiver in receiver_emails:
            server.sendmail(sender_email, receiver, message_to_send)
        print("EMAIL SENT..")
    except Exception as e:
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
            display = "FOR CITY : {} | {}".format(city, date)
            NO_SLOT_CITY = True
            city_message.append("\n\n")
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
                        session_text.append("DATE : {}".format(str(session["date"])))
                        session_text.append("AVAILABLE : {}".format(str(session["available_capacity"])))
                        session_text.append(str(session["vaccine"]))
                        session_text.append(str(session["slots"]))

                        #maps link
                        session_text.append("https://www.google.com/maps/place/" + str(session["address"]))
                        session_text.append("https://www.cowin.gov.in/home")
                        session_text.append("\n" * 1)

                        available = True
                        NO_SLOT_CITY = False
                        NO_SLOT_AT_ALL = False
                        x = "\n".join(session_text)
                        city_message.append(x)

                    if NO_SLOT_CITY:
                        message = "xxx NO SLOT AVAILABLE FOR {} Yr AT {} | PIN {} | {} xxx".format(AGE, str(session["name"]), str(session["pincode"]), date)
                        print(message)
                        city_message.append(message)

            if available:
                city_message.insert(0, "Subject: AVAILABLE | AGE: {} | CITY : {}, BOOK NOW".format(AGE, city))
                x = "\n".join(city_message)
                send_email(x, receiver_emails)
                available = False

    # if NO_SLOT_AT_ALL:
    #     send_email("Subject: CITY | {} | AGE {} | NO VACCINE SLOTS AVAILABLE"
    #                "\n"
    #                "\n"
    #                "{}"
    #                "\n"
    #                "\n"
    #                "{}".format(TODAYS_DATE, AGE, CITIES, DATES))






