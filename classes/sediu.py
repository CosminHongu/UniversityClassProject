from sqlalchemy.orm import relationship, validates
from base import Base
from sqlalchemy import Column, String, Integer, Date, Table, ForeignKey


class Sediu(Base):
    __tablename__ = 'sediu'

    #Many To Many
    personal_relationship = Table('personal_relationship', Base.metadata,
                                  Column('personal_id', Integer, ForeignKey('personal.id')),
                                  Column('sediu_id', Integer, ForeignKey('sediu.id')),

                                  )
    id = Column(Integer, primary_key=True)
    numarTelefon = Column(Integer)
    emailAddress = Column(String(100), nullable=False)
    denumire_sediu=Column(String(100), nullable=False)

    # Atributul back-populates este folosit pentru ca engine-ul sa intelelaga
    # ca este o relatie si sa populeze automat clasa copil cand clasa parinte este creata.

    address = relationship("Address", back_populates="sediu")
    address_id = Column(Integer, ForeignKey("address.id"))
    personal = relationship('Personal', secondary=personal_relationship)

    # setare getters & setters
    def __init__(self, numarTelefon, emailAddress, denumire_sediu="Scoala de soferi"):
        self.numarTelefon = numarTelefon
        self.emailAddress = emailAddress
        self.denumire_sediu = denumire_sediu

    #Validare Numar de Telefon
    @validates("numarTelefon")
    def validate_numarTelefon(self, key, numarTelefon):
        if len(str(numarTelefon)) != 10:
            raise ValueError("Numar de telefon incorect!")
        return numarTelefon

    # Modificare setters & getters O alta varianta fata de cea de sus
    #@hybrid_property
    #def email(self):
     #   return self.emailAddress

    #@email.setter
    #def email(self, email):
     #   self.emailAddress = email


