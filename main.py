from fastapi import FastAPI, Depends, status, Response, HTTPException
import models
from database import engine
from sqlalchemy.orm import Session
import database
import schemas

app = FastAPI()

models.base.metadata.create_all(engine)

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/api/forms/bogie-checksheet", status_code=status.HTTP_201_CREATED)
def create(request: schemas.BogieChecksheetRequest, db: Session = Depends(get_db)):
    try:
        new_form = models.BogieChecksheetForm(
            formNumber=request.formNumber,
            inspectionBy=request.inspectionBy,
            inspectionDate=request.inspectionDate,
            bogieDetails=models.BogieDetails(**request.bogieDetails.model_dump()),
            bogieChecksheet=models.BogieChecksheet(**request.bogieChecksheet.model_dump()),
            bmbcChecksheet=models.BMBCChecksheet(**request.bmbcChecksheet.model_dump())
        )
        db.add(new_form)
        db.commit()
        db.refresh(new_form)
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Failed to create bogie checksheet: {str(e)}")
    return {
        "data": {
            "inspectionBy": new_form.inspectionBy,
            "formNumber": new_form.formNumber,
            "inspectionDate": new_form.inspectionDate
        },
        "message": "Bogie checksheet submitted successfully.",
        "success": True
    }

@app.post("/api/forms/wheel-specifications", status_code=status.HTTP_201_CREATED)
def create_wheel_specification(request: schemas.WheelSpecificationForm, db: Session = Depends(get_db)):
    try:
        wheel_fields = models.WheelSpecificationFields(**request.fields.model_dump())
        db.add(wheel_fields)
        db.commit()
        db.refresh(wheel_fields)

        new_wheel_spec = models.WheelSpecificationForm(
            formNumber=request.formNumber,
            inspectionBy=request.inspectionBy,
            inspectionDate=request.inspectionDate,
            fields_id=wheel_fields.id
        )
        db.add(new_wheel_spec)
        db.commit()
        db.refresh(new_wheel_spec)
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Failed to create wheel specification: {str(e)}")
    return {
        "data": {
            "formNumber": new_wheel_spec.formNumber,
            "status": "Saved",
            "submittedBy": new_wheel_spec.inspectionBy,
            "submittedDate": new_wheel_spec.inspectionDate
        },
        "message": "Wheel specification submitted successfully.",
        "success": True
    }