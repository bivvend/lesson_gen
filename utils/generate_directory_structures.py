import os
from defines import SUBJECTS, LEVELS, YEAR_GROUPS_A_LEVEL, YEAR_GROUPS_GCSE, YEAR_GROUPS_LOWER
import json_structures
import json

import json_structures.course_structure

def create_directories_and_empty_structures_for_course(base_dir):
    # Iterate over each subject
    for subject in SUBJECTS:
        # Iterate over each level
        for level in LEVELS:
            # Handle LOWER_SCHOOL level
            if level.name == "LOWER_SCHOOL":
                for year_group in YEAR_GROUPS_LOWER:
                    # Create directory path
                    dir_path = os.path.join(base_dir, subject.name, level.name, year_group.name)
                    os.makedirs(dir_path, exist_ok=True)
                    print(f"Created directory: {dir_path}")
                    # Create an empty course structure file if it does not exist
                    course_structure_file = os.path.join(dir_path, "course_structure.json")
                    if not os.path.exists(course_structure_file):
                        with open(course_structure_file, "w") as f:
                            empty_course_structure = json_structures.course_structure.course_structure
                            empty_course_structure["subject"] = subject.name
                            empty_course_structure["level"] = level.name    
                            empty_course_structure["yearGroup"] = year_group.name
                            f.write(json.dumps(empty_course_structure, indent=4))  
                        
            # Handle GCSE level
            elif level.name == "GCSE":
                for year_group in YEAR_GROUPS_GCSE:
                    # Create directory path
                    dir_path = os.path.join(base_dir, subject.name, level.name, year_group.name)
                    os.makedirs(dir_path, exist_ok=True)
                    print(f"Created directory: {dir_path}")
                    # Create an empty course structure file if it does not exist
                    course_structure_file = os.path.join(dir_path, "course_structure.json")
                    if not os.path.exists(course_structure_file):
                        with open(course_structure_file, "w") as f:
                            empty_course_structure = json_structures.course_structure.course_structure
                            empty_course_structure["subject"] = subject.name
                            empty_course_structure["level"] = level.name    
                            empty_course_structure["yearGroup"] = year_group.name
                            f.write(json.dumps(empty_course_structure, indent=4)) 
            
            # Handle A_LEVEL level
            elif level.name == "A_LEVEL":
                for year_group in YEAR_GROUPS_A_LEVEL:
                    # Create directory path
                    dir_path = os.path.join(base_dir, subject.name, level.name, year_group.name)
                    os.makedirs(dir_path, exist_ok=True)
                    print(f"Created directory: {dir_path}")
                    # Create an empty course structure file if it does not exist
                    course_structure_file = os.path.join(dir_path, "course_structure.json")
                    if not os.path.exists(course_structure_file):
                        with open(course_structure_file, "w") as f:
                            empty_course_structure = json_structures.course_structure.course_structure
                            empty_course_structure["subject"] = subject.name
                            empty_course_structure["level"] = level.name    
                            empty_course_structure["yearGroup"] = year_group.name
                            f.write(json.dumps(empty_course_structure, indent=4))


def create_directories(base_dir):
    # Iterate over each subject
    for subject in SUBJECTS:
        # Iterate over each level
        for level in LEVELS:
            # Handle LOWER_SCHOOL level
            if level.name == "LOWER_SCHOOL":
                for year_group in YEAR_GROUPS_LOWER:
                    # Create directory path
                    dir_path = os.path.join(base_dir, subject.name, level.name, year_group.name)
                    os.makedirs(dir_path, exist_ok=True)
                    print(f"Created directory: {dir_path}")                      
            # Handle GCSE level
            elif level.name == "GCSE":
                for year_group in YEAR_GROUPS_GCSE:
                    # Create directory path
                    dir_path = os.path.join(base_dir, subject.name, level.name, year_group.name)
                    os.makedirs(dir_path, exist_ok=True)
                    print(f"Created directory: {dir_path}")
            
            # Handle A_LEVEL level
            elif level.name == "A_LEVEL":
                for year_group in YEAR_GROUPS_A_LEVEL:
                    # Create directory path
                    dir_path = os.path.join(base_dir, subject.name, level.name, year_group.name)
                    os.makedirs(dir_path, exist_ok=True)
                    print(f"Created directory: {dir_path}")
