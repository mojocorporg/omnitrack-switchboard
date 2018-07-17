from switchboard import settings
from sendsms.backends.base import BaseSmsBackend
import requests


def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


class CustomSMSBackend(BaseSmsBackend):
    def send_messages(self, messages):
        for message in messages:
            for to in message.to:
                try:
                    req = requests.get(
                        settings.get_secret("SOLUTIONSINFINI_URI") +
                        "?api_key=" +
                        settings.get_secret("SOLUTIONSINFINI_API_KEY") +
                        "&method=sms" +
                        "&message=" + message.body +
                        "&to=" + to +
                        "&sender=XPMOJO"
                    )
                    import pdb; pdb.set_trace()
                except:
                    if not self.fail_silently:
                        raise
