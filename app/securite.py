import hashlib
import hmac
import secrets

SEPARATEUR = "$"


def _deriver(mot_de_passe: str, sel: bytes) -> bytes:
    return hashlib.scrypt(mot_de_passe.encode(), salt=sel, n=2**14, r=8, p=1)


def hacher_mot_de_passe(mot_de_passe: str) -> str:
    sel = secrets.token_bytes(16)
    return f"{sel.hex()}{SEPARATEUR}{_deriver(mot_de_passe, sel).hex()}"


def verifier_mot_de_passe(mot_de_passe: str, mot_de_passe_hache: str) -> bool:
    sel, attendu = mot_de_passe_hache.split(SEPARATEUR)
    return hmac.compare_digest(_deriver(mot_de_passe, bytes.fromhex(sel)).hex(), attendu)
