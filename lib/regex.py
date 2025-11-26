import re

# Name regex (example from previous labs)
name_regex = re.compile(
    r"^[A-Z][a-z]+(?:['-][A-Z][a-z]+)*$"
)

# Phone number regex (example pattern)
phone_regex = re.compile(
    r"^\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$"
)

# Email regex: only allows emails starting with a letter
email_regex = re.compile(
    r"^[A-Za-z][\w.+-]*@[A-Za-z0-9-]+\.[A-Za-z0-9.-]+$"
)

# Regex for the bonus lab (matches specific sentences)
my_regex = re.compile(
    r"(It's such a lovely day today\.|Some weather we're having today, huh\?|Maybe today's just not my day\.)"
)
