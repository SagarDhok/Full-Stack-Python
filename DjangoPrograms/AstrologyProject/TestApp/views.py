from django.shortcuts import render
import datetime
import random

# Create your views here.


def result_view(request):
    msg_list = [
        "The stars align for your success—just wait for the perfect moment.",
        "Your destiny is written in the stars, and it’s brighter than ever.",
        "Soon, the universe will grant you the clarity you've been seeking.",
        "A life-changing opportunity is on the horizon—prepare yourself.",
        "The cosmos is smiling upon you, and your efforts will soon pay off.",
        "The energy around you is shifting—get ready for good news.",
        "In the next few days, you’ll find yourself in the right place at the right time.",
        "Love and luck will cross your path when you least expect it.",
        "Your dreams are about to take flight—hold onto your faith.",
        "Trust the process, for soon the universe will guide you exactly where you need to go.",
        'The golden days ahead',
        'Better to sleep more tim even in classroom',
        'Tomorrow will be the best day of your life',
        'Tomorrow is the prefect day to propose ur GF',
        'Very soon you will get job'
    ]

    names_list = ["Deepika", "Priyanka", "Katrina", "Alia", "Kareena", "Anushka", "Kriti", "Jacqueline", "Shraddha", "Sonam", "Madhuri", "Rani", "Vidya", "Sridevi", "Aishwarya", "Tapsee", "Kangana", "Bhumi", "Parineeti", "Disha"]




    time = datetime.datetime.now()
    h = int(time.strftime("%H"))
    if h<12:
        s = "GOOD MORNING"
    elif h<16:
        s = "GOOD AFTERNOON"
    elif h<21:
        s = "GOOD EVENING"
    else:
        s = "GOOD NIGHT"

        
    msg = random.choice(msg_list)
    name = random.choice(names_list)
    

    mydict = {"time":time,"name":name,"msg":msg,"wish":s}
    return render(request,template_name="testapp\\result.html",context=mydict)

