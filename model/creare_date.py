from base import Session, Base, engine
from cont import Cont
from cursant import Cursant
from instructor import Instructor
from pachet_ore import PachetOre

from personal import Personal
from personal_administrativ import PersonalAdministrativ
from sediu import Sediu
from address import Address
from vehicul import Vehicul


def adaugare_instructor(instructor, cont, vehicul, personal):
    instructor.cont = cont
    instructor.vehicul = vehicul
    instructor.personal = personal
    return instructor

def adaugare_personal_administrativ(personal_adm, cont, personal):
    personal_adm.cont = cont
    personal_adm.personal = personal

    return personal_adm

def create_all():
    session = Session()

    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    # Creare cont pentru instructori
    instructor_cont1 = Cont("user_inst1", "parola1", 1)
    instructor_cont2 = Cont("user_inst2", "parola2", 1)
    instructor_cont3 = Cont("user_inst3", "parola3", 1)

    # Creare instructori respectivi | Cont instructor, Vehicul, Personal respectiv
    instructor1 = adaugare_instructor(Instructor(), instructor_cont1, vehicul1, personal1)
    instructor2 = adaugare_instructor(Instructor(), instructor_cont2, vehicul2, personal2)
    instructor3 = adaugare_instructor(Instructor(), instructor_cont3, vehicul3, personal3)

 #Creare pachet_ore
pachet_ore1 = PachetOre(30)
pachet_ore2 = PachetOre(15)
pachet_ore1.instructor_id = 1
pachet_ore2.instructor_id = 2

#Creare Cursant:
cursant1 = Cursant("Popescu", "Marius", "10/10/2001" )
cursant.cont = Cont("user1", "parola1", 0)

# Sediu | Numar telefon, Email address
   sediu_alexandru = Sediu('0230562526', 'dsrp.alexandru@gmail.com')
   sediu_pacurari = Sediu('0230585642', 'dsrp.pacurari@gmail.com')
   sediu_nicolina = Sediu('0230568569', 'dsrp.nicolina@gmail.com')
   sediu_copou = Sediu('0758598698', 'dsrp.copou@gmail.com')

   # Address | Strada, oras, tara, cod postal, Judet
   adress_alexandru = Address('Sos. Nationala', 'Iasi', 'Romania', 700101, 'Iasi')
   adress_pacurari = Address('Str. Luca Arbore', 'Iasi', 'Romania,',700102, 'Iasi')
   adress_nicolina = Address('Str. Frumoasa', 'Iasi', 'Romania,', 700152, 'Iasi')
   adress_copou = Address('Str. Codrescu', 'Iasi', 'Romania', 700856, 'Iasi')
   adress5 = Address('Strada5', 'Oras5', 'Tara1,', 1235, 'Judet3')

   # Personal | Nume, prenume
   personal_alexandru1 = Personal("Ghiata", "Anamaria")
   personal_alexandru2=Personal("Abaza", "Andreea")
   personal_pacurari1 = Personal("Hongu", "Cosmin")
   personal_pacurari2=Personal("Abaza", "Bianca")
   personal_nicolina1=Personal("Raus", "Ana")
   personal_nicolina2=Personal("Popescu", "Corina")
   personal_copou1=Personal("Macaru", "Iraida")
   personal_copou2=Personal("Socolenco", "Natalia")
   personal_copou3=Personal("Gradinaru", "Augustin")

