from pydantic import BaseModel
from typing import Dict

from pydantic import BaseModel
from typing import Dict

class BMBCChecksheet(BaseModel):
    adjustingTube: str
    cylinderBody: str
    pistonTrunnion: str
    plungerSpring: str
    
    class Config:
        from_attributes = True

class BogieChecksheet(BaseModel):
    axleGuide: str
    bogieFrameCondition: str
    bolster: str
    bolsterSuspensionBracket: str
    lowerSpringSeat: str
    
    class Config:
        from_attributes = True

class BogieDetails(BaseModel):
    bogieNo: str
    dateOfIOH: str
    deficitComponents: str
    incomingDivAndDate: str
    makerYearBuilt: str
    
    class Config:
        from_attributes = True

class BogieChecksheetRequest(BaseModel):
    formNumber: str
    inspectionBy: str
    inspectionDate: str
    bogieDetails: BogieDetails
    bogieChecksheet: BogieChecksheet
    bmbcChecksheet: BMBCChecksheet
    
    class Config:
        from_attributes = True


class WheelSpecificationFields(BaseModel):
    axleBoxHousingBoreDia: str
    bearingSeatDiameter: str
    condemningDia: str
    intermediateWWP: str
    lastShopIssueSize: str
    rollerBearingBoreDia: str
    rollerBearingOuterDia: str
    rollerBearingWidth: str
    treadDiameterNew: str
    variationSameAxle: str
    variationSameBogie: str
    variationSameCoach: str
    wheelDiscWidth: str
    wheelGauge: str
    wheelProfile: str
    
    class Config:
        from_attributes = True
        
        
class WheelSpecificationForm(BaseModel):
    fields: WheelSpecificationFields
    formNumber: str
    inspectionBy: str
    inspectionDate: str
    
    
    class Config:
        from_attributes = True