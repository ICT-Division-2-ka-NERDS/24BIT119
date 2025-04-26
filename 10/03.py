# 24bit119

# Que-3

def make_vcard():
    name  = input("Full Name: ")
    phone = input("Phone no. (digits only): ")
    email = input("Email Address: ")

    vcard = f"BEGIN:VCARD\nVERSION:3.0\nFN:{name}\nTEL;TYPE=CELL:{phone}\nEMAIL:{email}\nEND:VCARD"

    filename = name.replace(" ", "_") + ".vcf"
    with open(filename, "w") as f:
        f.write(vcard)

    print(f"Saved vCard to {filename} in current directory.")

if __name__ == "__main__":
    make_vcard()
