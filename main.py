import cloudscraper
import threading
import json
import time

# student id = 1169
# term id = 36

def get_registration_list(student_id, start=0, length=10, term_id=36):
    scraper = cloudscraper.create_scraper(delay=10, browser="chrome")
    log_message = ""
    try:
        data = scraper.get(f"https://sisauppdemo.sisaupp.com/profile/get-student-available-courses?start={ start }&length={ length }&student_id={ student_id }&term_id={ term_id }&_=1718879707908&search[value]=&search[regex]=false")
        log_message = data.text
        get_registration = data.json()
        
        get_course_conflict()

    except Exception as error:
        get_registration = {"draw":0,"iTotalRecords":0,"iTotalDisplayRecords":0,"aaData": []}
        with open("error.log", "w") as f:
            f.write(f"Error: { error }:  { log_message }")

        return error

    total_fields = get_registration["iTotalRecords"]

    if start > total_fields:
        print( "go through all field!" )
    else:
        # time.sleep(5)
        print(f"going through field { start } for student { student_id }")
        return get_registration_list(student_id, start+1)


def get_course_conflict(course_id=0, section_id=0):
    scraper = cloudscraper.create_scraper(delay=10, browser="chrome")
    try:
        check_conflict = scraper.get("https://sisauppdemo.sisaupp.com/student/pre-registration/check-schedule-conflict/3639/1169").json()
    except Exception:
        check_conflict = {"status": "error", "message": "Something went wrong!"}

    return check_conflict


student_ids = [1169, 2785, 2786, 2783]
threads = []

for student_id in student_ids:
    t = threading.Thread(target=get_registration_list, args=(student_id,))
    threads.append(t)

    t.start()

for t in threads:
    t.join()


print("All threads are done!")
