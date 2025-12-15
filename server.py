from fastapi import FastAPI, Body,HTTPException
from typing import List
from pydantic import BaseModel
from datetime import date
import db_helper


app = FastAPI()

class Expense(BaseModel):
    amount: float
    category: str
    notes: str

class DateRange(BaseModel):
    start_date: date
    end_date: date







# GET endpoint
@app.get("/expenses/{expense_date}", response_model=List[Expense])
def get_expenses(expense_date: date):
    # just a placeholder in-memory DB
    return []

# POST endpoint
@app.post("/expenses/{expense_date}")
def add_or_update_expense(expense_date: date, expenses: List[Expense] = Body(...)):
    # just a placeholder
    return {"message": "Expenses added successfully"}


@app.post("/analytics/")
def get_analytics(date_range: DateRange):
    data= db_helper.fetch_expense_summary(date_range.start_date,date_range.end_date)
    if data is None:
        raise HTTPException(status_code=500,detail="Failed to retrieve expense summary")
    total= sum([row['total'] for row in data])
    breakdown={}

    for row in data:
        percentage= (row['total']/total)*100 if total!=0 else 0
        breakdown[row['category']]={
            'total':row['total'],
            'percentage': percentage
        }
    return breakdown












