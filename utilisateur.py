import hashlib
def hasher_mdp(mot_de_passe):
 """Retourne le hash SHA-256 du mot de passe."""
 return hashlib.sha256(mot_de_passe.encode()).hexdigest()
def verifier_mdp(mot_de_passe_saisi, hash_stocke):
 """Retourne True si le mot de passe correspond au hash."""
 return hasher_mdp(mot_de_passe_saisi) == hash_stocke