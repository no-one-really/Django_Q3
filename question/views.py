from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from question import serializers
from django.http import HttpResponse
from question.models import slots,point1,itemsinput





class Question1View(APIView):
    """Question1"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIView features"""


        return Response({'message': 'Hello!'})



    def post(self, request):
        """create a msg"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            k1=itemsinput(inputitem=name)
            k1.save()

            splitted_list=[]
            resu=itemsinput.objects.all()

            for lp in resu:
                splitted_list.append(lp.inputitem)


            positive_num=[]
            unwanted_val=[]
            sum=0
            numbers=0
            for i in splitted_list :
                try:
                    if(int(i)>0):
                        sum+=int(i)
                        numbers+=1
                        positive_num.append(i)
                    else:
                        unwanted_val.append(i)
                except :
                    unwanted_val.append(i)
            try:
                minimum=min(positive_num)
                maximum=max(positive_num)
            except:
                minimum=0
                maximum=0
            average=sum/numbers
            valid_entries = f' {len(positive_num)}'
            invalid_entries= f'{len(unwanted_val)}'
            return Response({'valid_entries': valid_entries,'invalid_entries':invalid_entries,"min":{minimum},"max":{maximum},"average":{average}})

        else:
            return Response(serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
            )

def Question2View(request):
    """Question2"""
    results=slots.objects.all()
    qw=[]
    er=[]
    for jk in results:
        qw.append(jk.name)
        er.append(jk.slot)
    my_dict = {str(i):er.count(i) for i in er}

    if request.POST:



        if '_book' in request.POST:
            slot_no = request.POST['slot']
            name_for_booking =  request.POST['name']

            try:
                if (int(slot_no)>=0) and (int(slot_no)<24):
                    if(my_dict[slot_no]<2):
                        r1=slots(slot=slot_no,name=name_for_booking)
                        r1.save()
                        return HttpResponse('slot booked')
                    else:

                        results = slots.objects.all()
                        return render(request, 'slotfull.html', {'slots': results})
                else:
                    return HttpResponse('give a valid entry')
            except:
                if (int(slot_no)>=0) and (int(slot_no)<24):

                     r1=slots(slot=slot_no,name=name_for_booking)
                     r1.save()
                     return HttpResponse('first booking of this slot')

            # if (len(listname)<=2):
            # if name not in (qw):
            #
            #     return HttpResponse('booked')
            # else:
            #     return HttpResponse('already booked')


        elif '_cancel' in request.POST:
            slot_no = request.POST['slot']
            name_for_booking =  request.POST['name']
            try:
                instance = slots.objects.filter(slot=slot_no,name=name_for_booking)
                instance.delete()
                return HttpResponse( 'your slot is cancelled' )
            except:
                return HttpResponse('you have not booked a slot to cancel it')


    return render(request,"question2.html")

class Point:

    def __init__(self, x, y):

        self.x = x
        self.y = y

def distSq(p, q):
     return (p.x - q.x) * (p.x - q.x) +(p.y - q.y) * (p.y - q.y)

def isSquare(p1, p2, p3, p4):
    d2 = distSq(p1, p2)
    d3 = distSq(p1, p3)
    d4 = distSq(p1, p4)
    if d2 == 0 or d3 == 0 or d4 == 0:
        return False
    if d2 == d3 and 2 * d2 == d4 and  2 * distSq(p2, p4) == distSq(p2, p3):
        return True
    if d3 == d4 and 2 * d3 == d2 and 2 * distSq(p3, p2) == distSq(p3, p4):
        return True
    if d2 == d4 and 2 * d2 == d3 and 2 * distSq(p2, p3) == distSq(p2, p4):
        return True
    return False


class Question3View(APIView):
    """Question3"""
    serializer_class = serializers.SquareSerializer

    def get(self, request, format=None):
        """Returns a list of APIView features"""


        return Response({'message': 'Hello!', 'an_apiview': 'alteast four entries are required'})

    def post(self, request):
        """create a msg"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            x = serializer.validated_data.get('x')
            y = serializer.validated_data.get('y')
            r1=point1(x=x,y=y)
            r1.save()
            pts = point1.objects.all().count()
            if(pts<4):
                return Response({'message':'alteast four entries are required'})
            # elif(pts==4):
            #     pt1=point1.objects.get(id=1)
            #     pt2=point1.objects.get(id=2)
            #     pt3=point1.objects.get(id=3)
            #     pt4=point1.objects.get(id=4)
            #     return Response({'x1':'yt'})
            else:
                last_four = point1.objects.all().order_by('-id')[:4]
                last_four_in_ascending_order = reversed(last_four)
                x=[]
                y=[]
                for i in last_four_in_ascending_order:
                    x.append(i.x)
                    y.append(i.y)

                p1 = Point(x[0], y[0])
                p2 = Point(x[1], y[1])
                p3 = Point(x[2], x[2])
                p4 = Point(x[3], x[3])
                if isSquare(p1, p2, p3, p4):
                    return Response({'message':'it is a square','coordinates are':[(x[0],y[0]),(x[1],y[1]),(x[2],y[2]),(x[3],y[3])]})
                else:
                    return Response({'message':'not a square','x_coordinates are':[(x[0],y[0]),(x[1],y[1]),(x[2],y[2]),(x[3],y[3])]})




        else:
            return Response(serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
            )

def home(request):
    return render(request, "index.html")
