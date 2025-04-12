from django.shortcuts import render

# Create your views here.
def news_info(request):
              return  render(request,template_name="testapp/index.html")




def sports_info(request):
    head_msg = 'Sports Information'
    sub_msg1 = 'Present IPL is going on...'
    sub_msg2 = 'Yesterday won the match RCB'
    sub_msg3 = 'Today match was KKR vs LSG'
    my_dict = {'head_msg':head_msg,'sub_msg1':sub_msg1,'sub_msg2':sub_msg2,"sub_msg3":sub_msg3,"type":'sports'}
    return render(request,template_name="testapp/news.html",context=my_dict)

def movies_info(request):
        head_msg = "Movies Information"
        sub_msg1 = 'MAD square is very good movie'
        sub_msg2 = 'OG will come very soon....'
        sub_msg3 = 'Planning for Aashiqui-3 with Mahesh Sir & Sunny Leone'

        my_dict = {"head_msg":head_msg,"sub_msg1":sub_msg1,"sub_msg2":sub_msg2,"sub_msg3":sub_msg3,"type":'movies'}

        return render(request,template_name="testapp/news.html",context=my_dict,)


def politics_info(request):
    head_msg = 'Politics Information'
    sub_msg1 = 'India PM was Modi ji'
    sub_msg2 = 'AP CM was Chandra Babu Naidu'
    sub_msg3 = 'AP Dy Cm was Pawan Kalyan'
    my_dict = {'head_msg':head_msg,'sub_msg1':sub_msg1,'sub_msg2':sub_msg2,
	'sub_msg3':sub_msg3,"type":'politics'}
    return render(request,template_name="testapp/news.html",context=my_dict)


