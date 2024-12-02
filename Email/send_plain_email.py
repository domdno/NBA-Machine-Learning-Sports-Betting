import boto3
from datetime import datetime

def _send_plain_email(data):
    region_name = "us-east-1"
    todays_date = datetime.today().strftime("%Y-%m-%d")
    CHARSET = "UTF-8"

    # Create an SES client
    session = boto3.session.Session()
    client = session.client(
        service_name='ses',
        region_name=region_name
    )

    response = client.send_email(
    Destination={
        "ToAddresses": [
            "domdno@gmail.com",
            "mdno1234@gmail.com"
        ],
    },
    Message={
        "Body": {
            "Text": {
                "Charset": CHARSET,
                "Data": data,
            }
        },
        "Subject": {
            "Charset": CHARSET,
            "Data": f"Today's Picks: {todays_date}",
        },
    },
    Source="domdno@gmail.com",
)