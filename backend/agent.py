def decide_action(customer_reply):

    text = customer_reply.lower()

    if "tomorrow" in text or "pay" in text:
        return "PAYMENT_PROMISED"

    elif "cannot" in text or "later" in text:
        return "NEED_EXTENSION"

    elif "not paying" in text:
        return "REFUSED"

    return "UNCLEAR"
