# Author: Ilmari Takkunen
# Github: ilmaritak
#
#
from utils import handle_commands

# Vankiselli
def room1():
    room_name = "room1"
    room_description = "Olet omassa sellissäsi. Ovesi itään on auki."

    direction = handle_commands(room_name, room_description, valid_dirs=['i'])

    if direction == 'i':
        room2()

# Tyrmän käytävä
def room2():
    room_name = "room2"
    room_description = (
        "Olet hämärässä käytävässä. "
        "Lännessä on ovi selliin, etelässä vartijan koppi, "
        "pohjoisessa portaikko ja idässä siivouskomero."
    )

    direction = handle_commands(room_name, room_description, valid_dirs=['l', 'e', 'p', 'i'])

    if direction == 'l':
        room1()
    if direction == 'e':
        room3()
    if direction == 'i':
        room4()
    if direction == 'p':
        room5()

# Vartijan koppi
def room3():
    room_name = "room3"
    room_description = (
        "Olet vartijan kopissa. Sinun onneksesi vartija ei ole paikalla."
        "Pohjoisessa on ovi takaisin käytävään."
    )

    direction = handle_commands(room_name, room_description, valid_dirs=['p'])

    if direction == 'p':
        room2()

# Siivouskomero
def room4():
    room_name = "room4"
    room_description = (
        "Olet siivouskomerossa."
        "Komerossa haisee ummehtunut ja jokapuolella on likaisia siivousvälineitä."
        "Lännessä on ovi takaisin käytävään."
    )

    direction = handle_commands(room_name, room_description, valid_dirs=['l'])

    if direction == 'l':
        room2()


# Portaikko
def room5():
    room_name = "room5"
    room_description = (
        "Olet yläkertaan johtavassa portaikossa."
        "Poistumalla itään pääset yläkertaan."
        "Poistumalla etelään pääset takaisin alakerran käytävään."
    )

    direction = handle_commands(room_name, room_description, valid_dirs=['e', 'i'])

    if direction == 'e':
        room2()
    if direction == 'i':
        room6()

# 2. kerroksen käytävä
def room6():
    room_name = "room6"
    room_description = (
        "Olet hyvin valaistussa käytävässä."
        "Pohjoisessa on ovi vankilanjohtajan toimistoon, "
        "Etelässä on ruokavarasto ja idässä on ovi parvekkeelle."
        "Lännestä pääset takaisin potaikkoon."
    )

    direction = handle_commands(room_name, room_description, valid_dirs=['l', 'e', 'p', 'i'])

    if direction == 'l':
        room5()
    if direction == 'e':
        room7()
    if direction == 'i':
        room10()
    if direction == 'p':
        room8()

# Ruokavarasto
def room7():
    room_name = "room7"
    room_description = (
        "Olet vankien ruokavarastossa."
        "Tuoksuu ummehtuneelle ja pilantuneelle ruoalle."
        "Hyllyt ovat pullollaan erilaisia vangeille tarkoitettuja ruokia."
        "Pohjoisessa on ovi takaisin käytävään."
    )

    direction = handle_commands(room_name, room_description, valid_dirs=['p'])

    if direction == 'p':
        room6()

# Toimisto
def room8():
    room_name = "room8"
    room_description = (
        "Olet hämärässä käytävässä. "
        "Lännessä on ovi selliin, etelässä vartijan koppi, "
        "pohjoisessa portaikko ja idässä siivouskomero."
    )

    direction = handle_commands(room_name, room_description, valid_dirs=['l', 'e', 'p', 'i'])

    if direction == 'l':
        room1()
    if direction == 'e':
        room3()
    if direction == 'i':
        room4()
    if direction == 'p':
        room5()

# Asevarasto
def room9():
    room_name = "room2"
    room_description = (
        "Olet hämärässä käytävässä. "
        "Lännessä on ovi selliin, etelässä vartijan koppi, "
        "pohjoisessa portaikko ja idässä siivouskomero."
    )

    direction = handle_commands(room_name, room_description, valid_dirs=['l', 'e', 'p', 'i'])

    if direction == 'l':
        room1()
    if direction == 'e':
        room3()
    if direction == 'i':
        room4()
    if direction == 'p':
        room5()

# Parveke
def room10():
    room_name = "room10"
    room_description = (
        "Olet hämärässä käytävässä. "
        "Lännessä on ovi selliin, etelässä vartijan koppi, "
        "pohjoisessa portaikko ja idässä siivouskomero."
    )

    direction = handle_commands(room_name, room_description, valid_dirs=['l', 'e', 'p', 'i'])

    if direction == 'l':
        room1()
    if direction == 'e':
        room3()
    if direction == 'i':
        room4()
    if direction == 'p':
        room5()

# Paloportaikko
def room11():
    room_name = "room2"
    room_description = (
        "Olet hämärässä käytävässä. "
        "Lännessä on ovi selliin, etelässä vartijan koppi, "
        "pohjoisessa portaikko ja idässä siivouskomero."
    )

    direction = handle_commands(room_name, room_description, valid_dirs=['l', 'e', 'p', 'i'])

    if direction == 'l':
        room1()
    if direction == 'e':
        room3()
    if direction == 'i':
        room4()
    if direction == 'p':
        room5()

# Pääaula
def room12():
    room_name = "room2"
    room_description = (
        "Olet hämärässä käytävässä. "
        "Lännessä on ovi selliin, etelässä vartijan koppi, "
        "pohjoisessa portaikko ja idässä siivouskomero."
    )

    direction = handle_commands(room_name, room_description, valid_dirs=['l', 'e', 'p', 'i'])

    if direction == 'l':
        room1()
    if direction == 'e':
        room3()
    if direction == 'i':
        room4()
    if direction == 'p':
        room5()

# Parkkihalli
def room13():
    room_name = "room2"
    room_description = (
        "Olet hämärässä käytävässä. "
        "Lännessä on ovi selliin, etelässä vartijan koppi, "
        "pohjoisessa portaikko ja idässä siivouskomero."
    )

    direction = handle_commands(room_name, room_description, valid_dirs=['l', 'e', 'p', 'i'])

    if direction == 'l':
        room1()
    if direction == 'e':
        room3()
    if direction == 'i':
        room4()
    if direction == 'p':
        room5()

# Uloskäynnin eteinen
def room14():
    room_name = "room2"
    room_description = (
        "Olet hämärässä käytävässä. "
        "Lännessä on ovi selliin, etelässä vartijan koppi, "
        "pohjoisessa portaikko ja idässä siivouskomero."
    )

    direction = handle_commands(room_name, room_description, valid_dirs=['l', 'e', 'p', 'i'])

    if direction == 'l':
        room1()
    if direction == 'e':
        room3()
    if direction == 'i':
        room4()
    if direction == 'p':
        room5()

# Vartijoiden taukohuone
def room15():
    room_name = "room2"
    room_description = (
        "Olet hämärässä käytävässä. "
        "Lännessä on ovi selliin, etelässä vartijan koppi, "
        "pohjoisessa portaikko ja idässä siivouskomero."
    )

    direction = handle_commands(room_name, room_description, valid_dirs=['l', 'e', 'p', 'i'])

    if direction == 'l':
        room1()
    if direction == 'e':
        room3()
    if direction == 'i':
        room4()
    if direction == 'p':
        room5()

# Vartijoiden pukuhuone
def room16():
    room_name = "room2"
    room_description = (
        "Olet hämärässä käytävässä. "
        "Lännessä on ovi selliin, etelässä vartijan koppi, "
        "pohjoisessa portaikko ja idässä siivouskomero."
    )

    direction = handle_commands(room_name, room_description, valid_dirs=['l', 'e', 'p', 'i'])

    if direction == 'l':
        room1()
    if direction == 'e':
        room3()
    if direction == 'i':
        room4()
    if direction == 'p':
        room5()

# Sisäpiha
def room17():
    room_name = "room2"
    room_description = (
        "Olet hämärässä käytävässä. "
        "Lännessä on ovi selliin, etelässä vartijan koppi, "
        "pohjoisessa portaikko ja idässä siivouskomero."
    )

    direction = handle_commands(room_name, room_description, valid_dirs=['l', 'e', 'p', 'i'])

    if direction == 'l':
        room1()
    if direction == 'e':
        room3()
    if direction == 'i':
        room4()
    if direction == 'p':
        room5()

# Portinvartijan koppi
def room18():
    room_name = "room2"
    room_description = (
        "Olet hämärässä käytävässä. "
        "Lännessä on ovi selliin, etelässä vartijan koppi, "
        "pohjoisessa portaikko ja idässä siivouskomero."
    )

    direction = handle_commands(room_name, room_description, valid_dirs=['l', 'e', 'p', 'i'])

    if direction == 'l':
        room1()
    if direction == 'e':
        room3()
    if direction == 'i':
        room4()
    if direction == 'p':
        room5()

# Tankkausasema
def room19():
    room_name = "room2"
    room_description = (
        "Olet hämärässä käytävässä. "
        "Lännessä on ovi selliin, etelässä vartijan koppi, "
        "pohjoisessa portaikko ja idässä siivouskomero."
    )

    direction = handle_commands(room_name, room_description, valid_dirs=['l', 'e', 'p', 'i'])

    if direction == 'l':
        room1()
    if direction == 'e':
        room3()
    if direction == 'i':
        room4()
    if direction == 'p':
        room5()

# Ulkoamaailma
def room20():
    room_name = "room2"
    room_description = (
        "Olet hämärässä käytävässä. "
        "Lännessä on ovi selliin, etelässä vartijan koppi, "
        "pohjoisessa portaikko ja idässä siivouskomero."
    )

    direction = handle_commands(room_name, room_description, valid_dirs=['l', 'e', 'p', 'i'])

    if direction == 'l':
        room1()
    if direction == 'e':
        room3()
    if direction == 'i':
        room4()
    if direction == 'p':
        room5()

