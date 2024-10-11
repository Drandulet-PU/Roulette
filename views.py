from flask import Blueprint, request, g, redirect, url_for, render_template, abort, jsonify
import random
from data import image_paths


def register_routes(app):
    #Главная страница
    @app.route('/')
    def index():
        return render_template('index.html')
    
        
    #IQ тест ток для умных ок да?
    @app.route('/iq')
    def iq():
        return render_template('iq.html')
    
    @app.route('/spin', methods=['POST'])
    def spin():
        result = random.randint(0, 30)
        return jsonify({'result': result, \
                        'name': image_paths[result]["name"], \
                        'image': random.choice(image_paths[result]["data"])})
        
    # 404
    @app.errorhandler(404)
    def error404(error):
        return render_template('404.html')
        
    # 405
    @app.errorhandler(405)
    def error404(error):
        return render_template('405.html')