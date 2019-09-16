from flask import *
import mlab__
from rivers_ import River
app = Flask(__name__)
mlab__.connect()



@app.route('/')
def rivers():
   all_rivers_africa = River.objects(continent__="Africa")
   all_rivers_safrica = River.objects(continent__="S. America",length__lt=1000)

   return render_template('index.html', all_rivers_africa = all_rivers_africa, all_rivers_safrica = all_rivers_safrica)
   print(all_rivers)
   
if __name__ == '__main__':
  app.run( debug=True)
 