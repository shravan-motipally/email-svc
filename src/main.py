import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from email_client import EmailWrapper

app = FastAPI()


class EmailRequest(BaseModel):
    sender_email: str
    sender_name: str
    to_email: str
    to_name: str
    cc_email: str | None
    cc_name: str | None
    bcc_email: str | None
    bcc_name: str | None
    reply_to_email: str
    reply_to_name: str
    subject: str
    html_content: str


@app.post("/send_email")
def send_email(email_request: EmailRequest):
    try:
        # Create an instance of the EmailWrapper class
        email_wrapper = EmailWrapper(
            sender_email=email_request.sender_email,
            sender_name=email_request.sender_name,
            to_email=email_request.to_email,
            to_name=email_request.to_name,
            cc_email=email_request.cc_email,
            cc_name=email_request.cc_name,
            bcc_email=email_request.bcc_email,
            bcc_name=email_request.bcc_name,
            reply_to_email=email_request.reply_to_email,
            reply_to_name=email_request.reply_to_name,
            html_content=email_request.html_content,
        )
        email_wrapper.send_email(email_request.subject, email_request.html_content)
        return {"message": "Email sent successfully!"}
    except Exception as e:
        return {"message": f"Error sending email: {str(e)}"}


@app.get("/health")
def health_check():
    return {"status": "ok"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80)
