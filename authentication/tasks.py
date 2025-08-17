from celery import shared_task


@shared_task(
    bind=True, serializer="json", max_retries=3, name="example_send_welcome_email"
)
def example_send_welcome_email(self, user_email):
    return {"message": f"Welcome email sent successfully to {user_email}."}
