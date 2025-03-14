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
    base_dir_slides = os.path.join(base_dir, defines.SLIDES_DIR)

    def generate_dir(year_group):
        slide_dir = os.path.join(base_dir_slides, subject.name, level.name, year_group.name)
        os.makedirs(slide_dir, exist_ok=True)
        #Load the course structure file
        course_structure_file = os.path.join(base_dir_course, subject.name, level.name, year_group.name, defines.COURSE_STRUCTURE_FILE)
        print(f"Loading course structure file: {course_structure_file}")
        with open(course_structure_file, "r") as f:
            course_structure = json.load(f)
            #Iterate over lessons
            for lesson in course_structure["lessons"]:
                #Create slide sub dirs
                if len(lesson["lessonCode"]) > 0:
                    slide_dir = os.path.join(base_dir_slides, subject.name, level.name, year_group.name, lesson["lessonCode"])
                    os.makedirs(slide_dir, exist_ok=True)

                    slide_dir_1 = os.path.join(base_dir_slides, subject.name, level.name, year_group.name, lesson["lessonCode"], defines.SLIDES_SUB_DIR_IMAGES)
                    os.makedirs(slide_dir_1, exist_ok=True)

                    slide_dir_2 = os.path.join(base_dir_slides, subject.name, level.name, year_group.name, lesson["lessonCode"], defines.SLIDES_SUB_DIR_TEX)
                    os.makedirs(slide_dir_2, exist_ok=True)

                    slide_dir_3 = os.path.join(base_dir_slides, subject.name, level.name, year_group.name, lesson["lessonCode"], defines.SLIDES_SUB_DIR_PDF)
                    os.makedirs(slide_dir_3, exist_ok=True)

                    slide_dir_4 = os.path.join(base_dir_slides, subject.name, level.name, year_group.name, lesson["lessonCode"], defines.SLIDES_SUB_DIR_VIDEO)
                    os.makedirs(slide_dir_4, exist_ok=True)

                    print(f"Created slide directory: {slide_dir}")
                else:
                    print(f"Lesson code is empty - no lesson")
    
    # Iterate over each subject
    for subject in defines.SUBJECTS:
        # Iterate over each level
        for level in defines.LEVELS:
            # Handle LOWER_SCHOOL level
            if level.name == "LOWER_SCHOOL":
                for year_group in defines.YEAR_GROUPS_LOWER:
                    generate_dir(year_group)
       
            # Handle GCSE level
            if level.name == "GCSE":
                for year_group in defines.YEAR_GROUPS_GCSE:
                    generate_dir(year_group)

            # Handle A_LEVEL level
            elif level.name == "A_LEVEL":
                for year_group in defines.YEAR_GROUPS_A_LEVEL:
                    generate_dir(year_group)