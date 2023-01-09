from django.shortcuts import render
from django.http import HttpResponse


def new(req):
    return HttpResponse("new")


def login(req):
    return HttpResponse("login")


def logout(req):
    return HttpResponse("logout")
