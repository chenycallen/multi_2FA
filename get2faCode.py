import pyotp,re

file_ = './2fa.txt'
target_line = 1


with open(file_, "r") as f:
    lines = [row.strip() for row in f]

for i, line in enumerate(lines):
    if i == target_line-1:
        totp_secret = line


totp_secret = re.sub(r"\s+", "", totp_secret)

totp = pyotp.TOTP(totp_secret)
totp_code = totp.now()

print(f"No.{target_line}\n2FA： {totp_code}")