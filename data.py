import random

# Данные для зарегестрированного пользователя
login_name_for_authorize_user = "mel_test_123@gmail.ru"
password_for_authorize_user = "Qwerty!"

# Данные для нового пользователя: email, password, submitpassword

user_name_new_user = f"test__{random.randint(100,999)}@gmail.com"
password_new_user = str(random.randint(100, 999))

# Данные для нового пользователя: но неправильная маска  *******@*******.***
login_with_uncorrect_mask = f"test__{random.randint(100,999)}!mail.com"
