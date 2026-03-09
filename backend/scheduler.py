from database import check_due_emis

def run_reminder():

    customers = check_due_emis()

    for c in customers:

        message = f"""
        Hello {c['name']}.
        Your EMI of {c['emi_amount']} rupees
        is due on {c['emi_due_date']}.
        Please confirm payment.
        """

        print("Calling:", c["name"])
        print(message)
