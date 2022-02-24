from flask import Flask, render_template, request, url_for, flash, redirect, session
from . import app
from . import views

messages = [{'title': 'Message One',
             'content': 'Message One Content'},
            {'title': 'Message Two',
             'content': 'Message Two Content'
             }]
