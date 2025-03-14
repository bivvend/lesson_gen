import enum
#Definitions for the project
GCSE_SPEC_TEXT = "gcse_spec.txt"
A_LEVEL_SPEC_TEXT = "a_level_spec.txt"
# Path to the directory containing the pdf specifications
SPECIFICATIONS_DIR = "resources\\specifications"
# Path to the directory containing the extracted text from the pdf specifications
SPECIFICATION_TEXT_DIR = "resources\\specifications\\output"

COURSE_STRUCTURE_DIR = "course_structure"
COURSE_STRUCTURE_FILE = "course_structure.json"
LESSON_PLANS_DIR = "lesson_plans"

SUBJECTS = enum.Enum("SUBJECTS", [("PHYSICS",1)])
LEVELS = enum.Enum("LEVELS", [("LOWER_SCHOOL",1),("GCSE",2), ("A_LEVEL",3)])
YEAR_GROUPS_LOWER = enum.Enum("YEAR_GROUPS_LOWER", [("YEAR_7",1),("YEAR_8",2),("YEAR_9",3)])
YEAR_GROUPS_GCSE = enum.Enum("YEAR_GROUPS_GCSE", [("YEAR_10",1),("YEAR_11",2)])
YEAR_GROUPS_A_LEVEL = enum.Enum("YEAR_GROUPS_A_LEVEL", [("YEAR_12",1), ("YEAR_13",2)])
TERMS = enum.Enum("TERMS", [("AUTUMN",1),("SPRING",2),("SUMMER",3)])
