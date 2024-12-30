from typing import Optional
from pydantic import BaseModel

# TODO: There should be a validation using model_validate to guarantee that at
# least one attribute is not None
# https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel.model_validate
class UniversityForUpdate(BaseModel):
  budget_id: Optional[int]
  name: Optional[str]
  province: Optional[str]
  city: Optional[str]
  address: Optional[str]
  contact_email: Optional[str]