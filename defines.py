import enum
#Definitions for the project
GCSE_SPEC_TEXT = "gcse_spec.txt"
A_LEVEL_SPEC_TEXT = "a_level_spec.txt"
# Path to the directory containing the pdf specifications
SPECIFICATIONS_DIR = "resources\\specifications"
# Path to the directory containing the extracted text from the pdf specifications
SPECIFICATION_TEXT_DIR = "resources\\specifications\\output"

LEVELS = enum.Enum("LEVELS", [("LOWER_SCHOOL",1),("GCSE",2), ("A_LEVEL",3)])
SUBJECTS = enum.Enum("SUBJECTS", [("PHYSICS",1)])
YEAR_GROUPS = enum.Enum("YEAR_GROUPS", [("YEAR_7",1),("YEAR_8",1),("YEAR_9",1),("YEAR_10",1),("YEAR_11",1), ("YEAR_12",2), ("YEAR_13",3)])
TERMS = enum.Enum("TERMS", [("AUTUMN",1),("SPRING",2),("SUMMER",3)])
