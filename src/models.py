import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Personajes(Base):
    __tablename__ = 'persona'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    color_ojos = Column(String(250), nullable=False)
    color_cabello = Column(String(250), nullable=False)
    gender = Column(String(250), nullable=False)


class Planetas(Base):
    __tablename__ = 'planeta'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    diametro = Column(String(250))
    rotation = Column(String(250))
    poblacion = Column(String(250), nullable=False)
    terreno = Column(String(250), nullable=False)


class Usuarios(Base):
    __tablename__ = 'usuario'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    password = Column(String(250))
    correo = Column(String(250))
    name = Column(String(250), nullable=False)

class Favoritos(Base):
    __tablename__ = 'favorito'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuario.id'))
    usuario = relationship(Usuarios)
    planeta_id = Column(Integer, ForeignKey('planeta.id'))
    planet = relationship(Planetas)
    personaje_id = Column(Integer, ForeignKey('persona.id'))
    person = relationship(Personajes)
  



    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')