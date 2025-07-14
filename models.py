from database import base
from sqlalchemy import Column, Integer, String, Float

from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship, declarative_base


class BogieChecksheetForm(base):
    __tablename__ = "bogie_checksheet_forms"
    id = Column(Integer, primary_key=True)
    formNumber = Column(String)
    inspectionBy = Column(String)
    inspectionDate = Column(String)
    bogieDetails = relationship("BogieDetails", uselist=False, back_populates="form")
    bogieChecksheet = relationship("BogieChecksheet", uselist=False, back_populates="form")
    bmbcChecksheet = relationship("BMBCChecksheet", uselist=False, back_populates="form")

class BogieDetails(base):
    __tablename__ = "BogieDetails"
    id = Column(Integer, primary_key=True)
    formId = Column(Integer, ForeignKey("bogie_checksheet_forms.id"))
    bogieNo = Column(String)
    makerYearBuilt = Column(String)
    incomingDivAndDate = Column(String)
    deficitComponents = Column(String)
    dateOfIOH = Column(String)
    form = relationship("BogieChecksheetForm", back_populates="bogieDetails")

class BogieChecksheet(base):
    __tablename__ = "BogieChecksheet"
    id = Column(Integer, primary_key=True)
    formId = Column(Integer, ForeignKey("bogie_checksheet_forms.id"))
    axleGuide = Column(String)
    bogieFrameCondition = Column(String)
    bolster = Column(String)
    bolsterSuspensionBracket = Column(String)
    lowerSpringSeat = Column(String)
    form = relationship("BogieChecksheetForm", back_populates="bogieChecksheet")

class BMBCChecksheet(base):
    __tablename__ = "BmbcChecksheet"
    id = Column(Integer, primary_key=True)
    formId = Column(Integer, ForeignKey("bogie_checksheet_forms.id"))
    adjustingTube = Column(String)
    cylinderBody = Column(String)
    pistonTrunnion = Column(String)
    plungerSpring = Column(String)
    form = relationship("BogieChecksheetForm", back_populates="bmbcChecksheet")


class WheelSpecificationFields(base):
    __tablename__ = "WheelSpecificationFields"
    id = Column(Integer, primary_key=True, index=True)
    axleBoxHousingBoreDia = Column(String)
    bearingSeatDiameter = Column(String)
    condemningDia = Column(String)
    intermediateWWP = Column(String)
    lastShopIssueSize = Column(String)
    rollerBearingBoreDia = Column(String)
    rollerBearingOuterDia = Column(String)
    rollerBearingWidth = Column(String)
    treadDiameterNew = Column(String)
    variationSameAxle = Column(String)
    variationSameBogie = Column(String)
    variationSameCoach = Column(String)
    wheelDiscWidth = Column(String)
    wheelGauge = Column(String)
    wheelProfile = Column(String)
    # Relationship to form(s)
    forms = relationship("WheelSpecificationForm", back_populates="fields")

class WheelSpecificationForm(base):
    __tablename__ = "WheelSpecificationForm"
    id = Column(Integer, primary_key=True, index=True)
    fields_id = Column(Integer, ForeignKey("WheelSpecificationFields.id"))
    formNumber = Column(String)
    inspectionBy = Column(String)
    inspectionDate = Column(String)
    # Relationship to fields
    fields = relationship("WheelSpecificationFields", back_populates="forms")