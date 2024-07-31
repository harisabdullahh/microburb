import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Define the URL of the API endpoint
url = 'https://newsapi.org/v2/top-headlines?country=us&apiKey=07015e6bc8d64d908b29e02e2540eaa1'

# Send a GET request to the API
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()

    # Extract the first article
    if 'articles' in data and len(data['articles']) > 0:
        first_article = data['articles'][0]
        title = first_article.get('title', 'No title available')

        # Email configuration
        sender_email = 'email'
        receiver_email = 'daniel@thefullwiki.org'
        password = 'password'  # Replace with your Gmail password or App password

        # Create the email content
        subject = 'Top News Article Title'
        body = f'The title of the first article is: {title}'

        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        # Send the email
        try:
            with smtplib.SMTP('smtp.gmail.com', 587) as server:
                server.starttls()
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, msg.as_string())
            print('Email sent successfully.')
        except Exception as e:
            print(f'Failed to send email: {e}')
    else:
        print('No articles found.')
else:
    print(f'Failed to retrieve data: {response.status_code}')
