from django.shortcuts import render,HttpResponse,get_object_or_404,redirect
from .models import TradeFormDetails

from django.core.files.storage import FileSystemStorage
from datetime import datetime

# Create your views here.


def index(request):
    return render(request,'trades/index.html')


def trade_entry(request):
    if request.method=="POST":
        date_time_str=request.POST.get('date')
        try:
            date_time= datetime.strptime(date_time_str,"%Y-%m-%dT%H:%M") # time format
        except ValueError:
            date_time=None


        asset=request.POST.get('Asset')
        direction=request.POST.get('long_short')
        entry_price=request.POST.get('entry_price')
        exit_price=request.POST.get('exit_price')
        loat_size=request.POST.get('loat_size')
        risk_manage=request.POST.get('risk_manage')

        result_for_trade=request.POST.get('trade_result')
        reason_for_trade=request.POST.get('reason_for_trade')


        emotions=request.POST.get('emotions')
        you_learned=request.POST.get('you_learned')


        screenshot=request.FILES.get('screenshot') # handling file uploads

        Trade_details=TradeFormDetails.objects.create(
            date_time=date_time,
            asset=asset,
            direction=direction,
            entry_price=entry_price,
            exit_price=exit_price,
            loat_size=loat_size,
            risk_manage=risk_manage,
            trade_result=result_for_trade,
            reason_for_trade=reason_for_trade,
            emotions=emotions,
            you_learned=you_learned,
            screenshot=screenshot



        )
        Trade_details.save()    

        return render(request,"trades/trade-entry.html",{'success':'Registration Successfull'})






    return render(request,'trades/trade-entry.html')





def report_view(request):
    details=TradeFormDetails.objects.all()
    return render(request,'trades/report-page.html',{'form_details':details})


def delete_record(request,pk):
    record=get_object_or_404(TradeFormDetails,pk=pk)
    record.delete()
    return redirect(report_view)


def edit_trade(request, pk):
    trade = get_object_or_404(TradeFormDetails, pk=pk)

    if request.method == 'POST':
        date_time_str = request.POST.get('date')
        try:
            date_time = datetime.strptime(date_time_str, "%Y-%m-%dT%H:%M")
        except ValueError:
            date_time = None

        trade.date_time = date_time
        trade.asset = request.POST.get('Asset')
        trade.direction = request.POST.get('long_short')
        trade.entry_price = request.POST.get('entry_price')
        trade.exit_price = request.POST.get('exit_price')
        trade.loat_size = request.POST.get('loat_size')
        trade.risk_manage = request.POST.get('risk_manage')
        trade.trade_result = request.POST.get('trade_result')
        trade.reason_for_trade = request.POST.get('reason_for_trade')
        trade.emotions = request.POST.get('emotions')
        trade.you_learned = request.POST.get('you_learned')

        if request.FILES.get('screenshot'):
            trade.screenshot = request.FILES.get('screenshot')

        trade.save()
        return redirect('report-view')

    return render(request, 'trades/edit-form.html', {'trade': trade})