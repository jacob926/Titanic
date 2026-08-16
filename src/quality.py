from pydantic import BaseModel, Field, field_validator
from typing import Optional

class PassengerSchema(BaseModel):
    """
    Contrat de qualité de données pour un passager.
    Si une donnée ne respecte pas ces règles, elle sera rejetée du pipeline.
    """
    passenger_id: int
    survived: int = Field(..., ge=0, le=1)  # Doit être 0 ou 1
    pclass: int = Field(..., ge=1, le=3)     # Doit être 1, 2 ou 3
    sex: str
    age: float = Field(..., ge=0, le=120)    # Âge valide entre 0 et 120
    fare: float = Field(..., ge=0)           # Tarif positif ou nul
    embarked: str

    @field_validator('sex')
    def validate_sex(cls, value):
        valid_genders = ['male', 'female']
        if value.lower() not in valid_genders:
            raise ValueError(f"Sexe invalide: {value}. Doit être 'male' ou 'female'.")
        return value.lower()

    @field_validator('embarked')
    def validate_embarked(cls, value):
        valid_ports = ['C', 'Q', 'S', 'Unknown']
        if value not in valid_ports:
            raise ValueError(f"Port d'embarquement invalide: {value}")
        return value