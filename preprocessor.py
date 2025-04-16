import re
import pandas as pd

def preprocess(data):
    # Updated pattern for 12-hour format with am/pm (including Unicode space before am/pm)
    pattern = r'(\d{1,2}/\d{1,2}/\d{2,4}), (\d{1,2}:\d{2}\s?[apAP][mM]) - (.+)'

    # Extract messages with timestamps
    matches = re.findall(pattern, data)

    # Extract dates and messages
    extracted_dates = [match[0] + ", " + match[1] for match in matches]
    messages = [match[2] for match in matches]

    # Create DataFrame
    df = pd.DataFrame({'user_message': messages, 'message_date': extracted_dates})

    # Convert message_date to datetime (with AM/PM)
    df['message_date'] = pd.to_datetime(df['message_date'].astype(str).str.strip(), format='%d/%m/%y, %I:%M %p', errors='coerce')

    # Rename for simplicity
    df.rename(columns={'message_date': 'date'}, inplace=True)

    # Split user and message content
    users = []
    clean_messages = []
    for message in df['user_message']:
        entry = re.split(r'([\w\W]+?):\s', message, maxsplit=1)
        if len(entry) > 1:
            users.append(entry[1])
            clean_messages.append(entry[2])
        else:
            users.append('group_notification')
            clean_messages.append(entry[0])

    df['user'] = users
    df['message'] = clean_messages
    df.drop(columns=['user_message'], inplace=True)

    # Time features
    df['only_date'] = df['date'].dt.date
    df['year'] = df['date'].dt.year
    df['month_num'] = df['date'].dt.month
    df['month'] = df['date'].dt.month_name()
    df['day'] = df['date'].dt.day
    df['day_name'] = df['date'].dt.day_name()
    df['hour'] = df['date'].dt.hour
    df['minute'] = df['date'].dt.minute

    # Time period (in 24-hour format still, but you can display it as AM/PM if needed)
    period = []
    for hour in df['hour']:
        if pd.isna(hour):
            period.append(None)
        elif hour == 23:
            period.append("11PM-12AM")
        elif hour == 0:
            period.append("12AM-1AM")
        else:
            start = pd.to_datetime(str(hour), format="%H").strftime("%I%p")
            end = pd.to_datetime(str((hour + 1) % 24), format="%H").strftime("%I%p")
            period.append(f"{start}-{end}")

    df['period'] = period

    return df
