from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# from sqlalchemy.ext.automap import automap_base




app = Flask(__name__)
db = SQLAlchemy(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:wjdtjrdl1130!!@localhost:3306/shopping'
app.config['SECRET_KEY'] = "key"

with app.app_context():
    db.init_app(app)
    db.Model.metadata.reflect(db.engine)



from my_app.routes import (main_route,user_routes)
from my_app.models import model

app.register_blueprint(main_route.bp)
app.register_blueprint(user_routes.bp)
app.register_blueprint(model.bp)


    




if __name__ == '__main__':
    # app = create_app()
    app.run(debug=True)