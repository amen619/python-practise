def replace_domain(email_id, old_domain, new_domain):
    if "@" + old_domain in email_id:
        index = email_id.index("@" + old_domain)
        new_email = email_id[:index] + "@" + new_domain
        return new_email
    return email_id

print(replace_domain("nived@xyz.com", "abc.com", "xyz.com"))