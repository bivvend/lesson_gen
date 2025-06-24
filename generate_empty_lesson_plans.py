#Based on the course structure files created in the previous step, generate empty lesson plans for each lesson in the course structure
#This will be a JSON file with the lesson plan structure    

import os
import json
import defines
import json_structures
import json_structures.lesson_plan_structures

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.abspath(__file__))
    base_dir_course = os.path.join(base_dir, defines.COURSE_STRUCTURE_DIR)
    base_dir_plans = os.path.join(base_dir, defines.LESSON_PLANS_DIR)
    
    # Iterate over each subject
    for subject in defines.SUBJECTS:
        # Iterate over each level
        for level in defines.LEVELS:
            # Handle LOWER_SCHOOL level
            if level.name == "LOWER_SCHOOL":
                for year_group in defines.YEAR_GROUPS_LOWER:
                    #Load the course structure file
                    course_structure_file = os.path.join(base_dir_course, subject.name, level.name, year_group.name, defines.COURSE_STRUCTURE_FILE)
                    print(f"Loading course structure file: {course_structure_file}")
                    with open(course_structure_file, "r") as f:
                        course_structure = json.load(f)
                        #Iterate over lessons
                        for lesson in course_structure["lessons"]:
                            #Create the lesson plan file
                            lesson_plan_file = os.path.join(base_dir_plans, subject.name, level.name, year_group.name, defines.DRAFTS, f"empty_plan_{lesson["lessonCode"]}.json")
                            if not os.path.exists(lesson_plan_file):
                                print(f"Creating lesson plan file: {lesson_plan_file}")
                                if len(lesson["lessonCode"]) > 0:
                                    with open(lesson_plan_file, "w") as f:
                                        empty_lesson_plan = json_structures.lesson_plan_structures.lesson_plan_structure
                                        empty_lesson_plan["subject"] = subject.name
                                        empty_lesson_plan["level"] = level.name
                                        empty_lesson_plan["yearGroup"] = year_group.name
                                        empty_lesson_plan["lessonCode"] = lesson["lessonCode"]
                                        empty_lesson_plan["lessonTitle"] = lesson["lessonTitle"]
                                        f.write(json.dumps(empty_lesson_plan, indent = 4)) 
                                else:
                                    print(f"Lesson code is empty - no lesson")
                            else:
                                print(f"Lesson plan file already exists: {lesson_plan_file}")         
            # Handle GCSE level
            if level.name == "GCSE":
                for year_group in defines.YEAR_GROUPS_GCSE:
                    #Load the course structure file
                    #Load the course structure file
                    course_structure_file = os.path.join(base_dir_course, subject.name, level.name, year_group.name, "course_structure.json")
                    print(f"Loading course structure file: {course_structure_file}")
                    with open(course_structure_file, "r") as f:
                        course_structure = json.load(f)
                        #Iterate over lessons
                        for lesson in course_structure["lessons"]:
                            #Create the lesson plan file
                            lesson_plan_file = os.path.join(base_dir_plans, subject.name, level.name, year_group.name, defines.DRAFTS, f"empty_plan_{lesson["lessonCode"]}.json")
                            if not os.path.exists(lesson_plan_file):
                                print(f"Creating lesson plan file: {lesson_plan_file}")
                                if len(lesson["lessonCode"]) > 0:
                                    with open(lesson_plan_file, "w") as f:
                                        empty_lesson_plan = json_structures.lesson_plan_structures.lesson_plan_structure
                                        empty_lesson_plan["subject"] = subject.name
                                        empty_lesson_plan["level"] = level.name
                                        empty_lesson_plan["yearGroup"] = year_group.name
                                        empty_lesson_plan["lessonCode"] = lesson["lessonCode"]
                                        empty_lesson_plan["lessonTitle"] = lesson["lessonTitle"]
                                        empty_lesson_plan["contentItems"] = lesson["contentItems"]
                                        f.write(json.dumps(empty_lesson_plan, indent = 4)) 
                                else:
                                    print(f"Lesson code is empty - no lesson")
                            else:
                                print(f"Lesson plan file already exists: {lesson_plan_file}")          
            # Handle A_LEVEL level
            elif level.name == "A_LEVEL":
                for year_group in defines.YEAR_GROUPS_A_LEVEL:
                    #Load the course structure file
                    course_structure_file = os.path.join(base_dir_course, subject.name, level.name, year_group.name, "course_structure.json")
                    print(f"Loading course structure file: {course_structure_file}")
                    with open(course_structure_file, "r") as f:
                        course_structure = json.load(f)
                        #Iterate over lessons
                        for lesson in course_structure["lessons"]:
                            #Create the lesson plan file
                            lesson_plan_file = os.path.join(base_dir_plans, subject.name, level.name, year_group.name, defines.DRAFTS, f"empty_plan_{lesson["lessonCode"]}.json")
                            if not os.path.exists(lesson_plan_file):
                                print(f"Creating lesson plan file: {lesson_plan_file}")
                                if len(lesson["lessonCode"]) > 0:
                                    with open(lesson_plan_file, "w") as f:
                                        empty_lesson_plan = json_structures.lesson_plan_structures.lesson_plan_structure
                                        empty_lesson_plan["subject"] = subject.name
                                        empty_lesson_plan["level"] = level.name
                                        empty_lesson_plan["yearGroup"] = year_group.name
                                        empty_lesson_plan["lessonCode"] = lesson["lessonCode"]
                                        empty_lesson_plan["lessonTitle"] = lesson["lessonTitle"]
                                        f.write(json.dumps(empty_lesson_plan, indent = 4)) 
                                else:
                                    print(f"Lesson code is empty - no lesson")
                            else:
                                print(f"Lesson plan file already exists: {lesson_plan_file}")   


