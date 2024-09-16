from langchain_core.pydantic_v1 import BaseModel, Field

class Currency(BaseModel):
    currency: str = Field(description="Currency code")
    amount: float = Field(description="Amount of the currency")

class CutoffScoreDetails(BaseModel):
    year: int = Field(description="Year of the cutoff score")
    cutoff_score: float = Field(description="Cutoff score of the university")

class MajorDetails(BaseModel):
    major_id: str = Field(description="ID of the major")
    major_name: str = Field(description="Name of the major")
    major_cutoff_details: list[CutoffScoreDetails] = Field(description="Cutoff score details of the major")
    subject_combinations: list[str] = Field(description="Subject combinations of the major")
    tuition_fee: float = Field(description="Tuition fee of the major per year")
    note: str = Field(description="Notes about the major")

class AdmissionDetails(BaseModel):
    year: int = Field(description="Year of the application details")
    admission_target: int = Field(description="Admission target of the university")
    methods: list[str] = Field(description="Methods of admission")

class UniversityContact(BaseModel):
    location: str = Field(description="Location of the university")
    phone: list[str] = Field(description="Phone number(s) of the university")
    website: str = Field(description="Website of the university")
    email: str = Field(description="Email of the university")

class University(BaseModel):
    id: str = Field(description="ID of the university")
    name: str = Field(description="Name of the university")
    region: str = Field(description="Region where the university is located")
    contact: UniversityContact = Field(description="Contact details of the university")
    admission_details: AdmissionDetails = Field(description="Admission details of the university")
    
    