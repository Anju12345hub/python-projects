import datetime
exam_timeline=input("enter name and date of exam with colon separation \n ")
exam_timeline_list=exam_timeline.split(":")
exam_name=exam_timeline_list[0]
exam_date=exam_timeline_list[1]
dead_line=datetime.datetime.strptime(exam_date,"%d-%m-%Y")
today_date=datetime.datetime.today()
till_day=dead_line-today_date
print(f"so,You have {till_day} are left for your exam {exam_name}")
