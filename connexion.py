import mysql.connector
from mysql.connector import Error
CONFIG = {
 "host" : "localhost", 
 "user" : "root",
 "password" : "",
"database" : "taskflow_db", 
 "charset" : "utf8mb4"
}
def obtenir_connexion():
 """
 Ouvre et retourne une connexion a la base de donnees.
 Retourne None si la connexion echoue.
 
 Utilisation dans les autres modules :
 conn = obtenir_connexion()
 if conn:
 # faire des requetes
 conn.close()
 """
 # PISTE : utilisez mysql.connector.connect(**CONFIG)
 # Gerez l'exception Error pour afficher un message propre
 pass
def fermer_connexion(conn):
 """
 Ferme proprement la connexion si elle est ouverte.
 
 PISTE : verifiez que conn n'est pas None avant d'appeler conn.close()
 """
 pass
def fermer_connexion(conn):
 """
 Ferme proprement la connexion si elle est ouverte.
 
 PISTE : verifiez que conn n'est pas None avant d'appeler conn.close()
 """
 pass