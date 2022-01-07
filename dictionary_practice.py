
#the naughty list dictionary practice
the_naughty_list = {"Yujing": False, "Angelina": False, "Barbie": True}

naughty_status = the_naughty_list.get("Angelina")
print("Angelina is...", naughty_status)

#secret santa practice
secret_santa_list = {"Elfie": "Ruldolf"}

who_got_elfie = secret_santa_list.get("Elfie")
print("Who is Elfie's secret santa?", who_got_elfie)

