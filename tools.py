import os


def create_credentials():
    cred = os.listdir(os.getcwd())
    if not "credentials.py" in cred:
        print("Credentials are not set yet")
        from_email = input("Enter sender email")
        password = input("Enter sender password")
        to_email = input("Enter receiver email")
        creed_file = open("credentials.py", 'w')
        creed_file.write(f"""
            FROM_EMAIL = {from_email}
            PASSWORD = {password}
            TO_EMAIL = {to_email}
        """)
        creed_file.close()


def create_record_file(file_name):
    folder_path = f"{os.getcwd()}/scraped_items/"
    files = os.listdir(folder_path)
    for file in files:
        if file == file_name:
            os.remove(f"{folder_path}{file_name}")
    file = f"{folder_path}{file_name}"
    file = open(file, "w")
    file.close()
