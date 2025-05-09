from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from .personne_model import PERSONNE

class ADMINISTRATEUR(PERSONNE):
    __tablename__ = "administrateurs"

    id = Column(Integer, ForeignKey("personnes.id"), primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    password_hash = Column(String(128), nullable=False)
    role = Column(String(50), nullable=False, default="administrateur")
    created_at = Column(DateTime, nullable=False)
    last_login = Column(DateTime, nullable=True)
    is_active = Column(Boolean, default=True)
    super_admin = Column(Boolean, default=False)
