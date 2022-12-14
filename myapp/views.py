from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import MonthSerializer,UserSerializer
from .models import months,user
from django.shortcuts import get_object_or_404
import datetime









class MonthViews(APIView):
    # create month
    
    queryset = months.objects.all()
    # serializer_class = MonthSerializer
    def post(self, request):
        serializer = MonthSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data},status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


    # get month
    def get(self, request, id=None):
        try:
         if id:
            month = months.objects.get(month_id=id)
            serializer = MonthSerializer(month)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

         monthss = months.objects.all()
         serializer = MonthSerializer(monthss, many=True)
         return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
         return Response({'status':'error','message':'item does not exists'})



    # update month
    def patch(self, request, id=None):
        month = months.objects.get(month_id=id)
        serializer = MonthSerializer(month, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors})


    # delete month
    def delete(self, request, id=None):
        item = months.objects.all()
        item.delete()
        return Response({"status": "success", "data": "Item Deleted"})





class UserViews(APIView):
    queryset = user.objects.all()
    # create user
    def post(self, request):
        
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


    # get user
    def get(self, request, id=None):
        try:
         if id:
            item = user.objects.get(user_id=id)
            serializer = UserSerializer(item)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

         items = user.objects.all()
         serializer = UserSerializer(items, many=True)
         return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
         return Response({'status':'error','message':'item does not exists'})



    # update user
    def patch(self, request, id=None):
        item = user.objects.get(user_id=id)
        serializer = UserSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors})


    # delete user
    def delete(self, request, id=None):
        item = get_object_or_404(user, user_id=id)
        item.delete()
        return Response({"status": "success", "data": "Item Deleted"})




class CompletePayment(APIView):
    
    queryset = user.objects.all()
    def post(self,request):

        email = request.data['email']
        # current month 
        currMonth = datetime.datetime.now().strftime("%B")
       
        try:
            # searching for user 
            usrr = user.objects.get(email=email)

            usrr.monthsPaid = currMonth
            usrr.paid = True
            # payment function here
            usrr.save()
            return Response({"status": "success", "data":"payment successfull",'email':email}, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({'status':'error','message':'user not registered','uu':usrr})
