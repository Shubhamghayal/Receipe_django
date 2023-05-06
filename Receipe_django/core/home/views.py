from django.shortcuts import render
def home(request):
    peoples =[
        {'name':'shubham' , 'age':25},
        {'name': 'muchhi', 'age': 55},
        {'name': 'rasal', 'age': 21},
    ]
    for people in peoples:
        print(people)


    return render(request,'index.html',context={'peoples': peoples})


