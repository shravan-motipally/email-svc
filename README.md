# Email Service

This is an email service created in Python using Brevo API.

## Installation

To install this project, you can clone the repository and run the following command:

```bash
pip install -r requirements.txt
```

## Usage

You need to have docker installed in your machine

To use this email service, you can run the following command:

```bash
docker compose up --build
```

Create an .env file in your local that will have the following environment variables.
```bash
BREVO_API_KEY=your_api_key
```

Open Postman or any other API client and make a POST request to the following endpoint:
```bash
curl --request POST \
  --url http://localhost:80/send_email \
  --header 'Content-Type: application/json' \
  --data '{
	"sender_email": "senderemail@email.com",
	"sender_name": "yourname",
	"to_email": "toemail@email.com",
	"to_name": "person you are sending email to",
	"cc_email": null,
	"cc_name": null,
	"bcc_email": null,
	"bcc_name": null,
	"reply_to_email": "sender email or your custom reply to email",
	"reply_to_name": "your name",
	"html_content": "<html><body><h1>Whatever you wish here</h1></body></html>",
	"subject": "Subject"
}'
```
