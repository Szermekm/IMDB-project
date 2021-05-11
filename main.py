from scraping import *
import gspread
import sys
import schedule
import time


def job():
    print("Job is running!")
    best_actors = scrape_top_chart()

    gc = gspread.service_account(filename='client_secret.json')

    actors_sheet = gc.create('actors')
    worksheet = actors_sheet.sheet1

    for index, actor in enumerate(best_actors, start=0):
        worksheet.update_cell(index+1, 1, actor[0])

    emails_sheet = gc.open_by_url(sys.argv[1])
    worksheet_emails = emails_sheet.sheet1
    emails_list = worksheet_emails.col_values(1)

    for email in emails_list:
        actors_sheet.share(email, perm_type='user', role='writer')
    print("Job finished!")

schedule.every().monday.at("00:00").do(job)
print("Job is scheduled to run every Monday at midnight!")

while True:
    schedule.run_pending()
    time.sleep(1)


