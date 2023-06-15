from django.shortcuts import render, redirect
from .models import Profile, Friend
from .forms import ChatMessageForm, ChatMessage
from django.http import JsonResponse
import json

# Create your views here.


def index(request):
    user = request.user.profile
    friends = user.friends.all()
    context = {'user': user, 'friends': friends}
    return render(request, 'mychat/index.html', context)


def detail(request, pk):
    friend = Friend.objects.get(profile_id=pk)
    user = request.user.profile
    profile = Profile.objects.get(id=friend.profile.id)
    chats = ChatMessage.objects.all()
    rec_chats = ChatMessage.objects.filter(
        mxg_sender=profile, mxg_reciver=user)
    rec_chats.update(seen=True)
    form = ChatMessageForm()
    # check the post method (is message or not in post)
    if request.method == 'POST':
        form = ChatMessageForm(request.POST)
        if form.is_valid():
            chat_message = form.save(commit=False)
            chat_message.mxg_sender = user
            chat_message.mxg_reciver = profile
            chat_message.save()
            return redirect('detail', pk=friend.profile.id)
    context = {'friend': friend, 'form': form,
               'user': user, 'chats': chats, 'profile': profile, 'num': rec_chats.count()}
    return render(request, 'mychat/detail.html', context)


def sentMessage(request, pk):
    user = request.user.profile
    friend = Friend.objects.get(profile_id=pk)
    profile = Profile.objects.get(id=friend.profile.id)
    data = json.loads(request.body)
    new_chat = data['msg']
    new_chat_message = ChatMessage.objects.create(
        body=new_chat, mxg_sender=user, mxg_reciver=profile, seen=False)
    print(new_chat)
    return JsonResponse(new_chat_message.body, safe=False)


def recivedMessage(request, pk):
    user = request.user.profile
    friend = Friend.objects.get(profile_id=pk)
    arr = []
    profile = Profile.objects.get(id=friend.profile.id)
    chats = ChatMessage.objects.filter(mxg_sender=profile, mxg_reciver=user)
    for chat in chats:
        arr.append(chat.body)

    return JsonResponse(arr, safe=False)


def chatNotification(request):
    user = request.user.profile
    friends = user.friends.all()
    arr = []
    for friend in friends:
        chats = ChatMessage.objects.filter(
            mxg_sender__id=friend.profile.id, mxg_reciver=user, seen=False)
        arr.append(chats.count())
    return JsonResponse(arr, safe=False)
