from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/calendar']

def authenticate_google_calendar():
    flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
    creds = flow.run_local_server(port=0)
    return creds

def create_event(creds, title, dt):
    service = build('calendar', 'v3', credentials=creds)
    event = {
        'summary': title,
        'start': {
            'dateTime': dt.isoformat(),
            'timeZone': 'Asia/Bangkok',
        },
        'end': {
            'dateTime': (dt + timedelta(hours=1)).isoformat(),
            'timeZone': 'Asia/Bangkok',
        },
        'reminders': {
            'useDefault': True,
        },
    }
    event = service.events().insert(calendarId='primary', body=event).execute()
    print(f"สร้างนัดหมายเรียบร้อย: {event.get('htmlLink')}")
