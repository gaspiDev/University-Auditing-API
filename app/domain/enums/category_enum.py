from enum import Enum

# TODO: Use from enum import StrEnum instead
class CategoryEnum(str, Enum):
    SALARIES = "salaries"
    UTILITIES = "utilities"
    MAINTENANCE = "maintenance"
    EQUIPMENT = "equipment"
    SUPPLIES = "supplies"
    RESEARCH_GRANTS = "research_grants"
    SCHOLARSHIPS = "scholarships"
    EVENTS = "events"
    TRAVEL = "travel"
    LIBRARY = "library"
    TECHNOLOGY = "technology"
    MARKETING = "marketing"
    FACILITY_RENTALS = "facility_rentals"
    STUDENT_SERVICES = "student_services"
    ADMINISTRATIVE = "administrative"
    MISCELLANEOUS = "miscellaneous"