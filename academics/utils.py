def send_results_sms(phone, message):
    """
    Simulated SMS sending function.
    In production, integrate with Africa's Talking or other SMS gateway.
    """
    print(f"SMS to {phone}: {message}")
    # For production:
    # import africastalking
    # africastalking.initialize(username, api_key)
    # sms = africastalking.SMS
    # sms.send(message, [phone])
    return True
